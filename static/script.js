/* ============================================================
   AyurDiag — front-end logic
   Sends messages to the Flask /chat endpoint and renders the
   reply as either a structured "diagnosis" card or a plain
   notice bubble (for validations / low-confidence replies).
   ============================================================ */

(function () {
    "use strict";

    var chatMessages = document.getElementById("chat-messages");
    var userInput = document.getElementById("user-input");
    var sendBtn = document.getElementById("send-btn");
    var micBtn = document.getElementById("mic-btn");
    var statusBar = document.getElementById("status-bar");
    var welcomeTime = document.getElementById("welcome-time");

    // ----------------------------------------------------------
    // Small helpers
    // ----------------------------------------------------------

    function nowLabel() {
        var now = new Date();
        var h = now.getHours();
        var m = now.getMinutes();
        var ampm = h >= 12 ? "PM" : "AM";
        h = h % 12;
        if (h === 0) h = 12;
        return h + ":" + (m < 10 ? "0" : "") + m + " " + ampm;
    }

    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Remove the status bar once the first exchange happens
    function hideStatusBar() {
        if (statusBar) {
            statusBar.style.display = "none";
        }
    }

    // ----------------------------------------------------------
    // Message wrappers
    // ----------------------------------------------------------

    function makeMessage(isUser, timestamp) {
        var wrapper = document.createElement("div");
        wrapper.className = isUser ? "message user-message" : "message bot-message";

        var time = document.createElement("span");
        time.className = "message-time";
        time.textContent = timestamp || nowLabel();

        wrapper.appendChild(time);
        chatMessages.appendChild(wrapper);

        setTimeout(function () {
            wrapper.classList.add("time-placed");
        }, 0);

        return wrapper;
    }

    function addUserMessage(text) {
        var wrapper = makeMessage(true);
        var bubble = document.createElement("div");
        bubble.className = "message-bubble user-bubble";
        bubble.textContent = text;
        wrapper.insertBefore(bubble, wrapper.firstChild);
        scrollToBottom();
        return wrapper;
    }

    var THINK_PHRASES = [
        "analyzing symptoms",
        "cross-referencing database",
        "comparing treatment paths",
        "formulating response"
    ];

    function addTypingIndicator() {
        var wrapper = makeMessage(false);
        var indicator = document.createElement("div");
        indicator.className = "typing-indicator";
        indicator.innerHTML =
            '<span class="typing-dots">' +
            '<span class="typing-dot"></span><span class="typing-dot"></span><span class="typing-dot"></span>' +
            '</span>' +
            '<span class="typing-label">analyzing symptoms…</span>';
        wrapper.insertBefore(indicator, wrapper.firstChild);

        var i = 0;
        var timer = setInterval(function () {
            i = (i + 1) % THINK_PHRASES.length;
            var label = wrapper.querySelector(".typing-label");
            if (label) label.textContent = THINK_PHRASES[i] + "…";
        }, 600);
        wrapper._typingTimer = timer;

        scrollToBottom();
        return wrapper;
    }

    // ----------------------------------------------------------
    // RENDERING — structured diagnosis card
    // The backend reply is standardized as numbered sections:
    //   1. Based on the symptoms ... **Disease**
    //   2. Ayurvedic Medicines:  (bulleted)
    //   3. Allopathic Medicines: (bulleted)
    //   4. <advice text>
    //   5. 🏥 Recommended Department: **Dept**
    //   6. Advice: <final note>
    // ----------------------------------------------------------

    function extractBullets(lines) {
        var items = [];
        lines.forEach(function (line) {
            var t = line.trim();
            if (t.indexOf("- ") === 0) {
                var item = t.slice(2).trim();
                if (item) items.push(item);
            }
        });
        return items;
    }

    function parseDiagnosis(text) {
        var lines = text.split(/\r?\n/);
        var result = {
            disease: null,
            ayurvedic: [],
            allopathic: [],
            advice: "",
            department: null,
            other: [],
            foot: ""
        };

        var sections = [];
        var current = null;

        lines.forEach(function (line) {
            var trimmed = line.trim();
            var sectionMatch = trimmed.match(/^(\d)\.\s*(.*)$/);
            if (sectionMatch && parseInt(sectionMatch[1], 10) >= 1 && parseInt(sectionMatch[1], 10) <= 6) {
                current = {
                    num: parseInt(sectionMatch[1], 10),
                    content: [sectionMatch[2]],
                    raw: trimmed
                };
                sections.push(current);
            } else if (current) {
                current.content.push(trimmed);
            }
        });

        sections.forEach(function (sec) {
            var joined = sec.content.join(" ");
            var strong = joined.match(/\*\*(.+?)\*\*/);
            switch (sec.num) {
                case 1:
                    result.disease = strong ? strong[1] : joined.replace(/\*\*/g, "").trim();
                    break;
                case 2:
                    result.ayurvedic = extractBullets(sec.content);
                    break;
                case 3:
                    result.allopathic = extractBullets(sec.content);
                    break;
                case 4:
                    if (sec.content.length) {
                        result.advice = sec.content
                            .join(" ")
                            .replace(/\*\*/g, "")
                            .replace(/📌.*$/g, "")
                            .trim();
                    }
                    break;
                case 5:
                    result.department = strong
                        ? strong[1]
                        : joined.replace(/[🏥📌]/g, "").replace("Recommended Department:", "").replace(/\*\*/g, "").trim();
                    break;
                case 6:
                    result.foot = sec.content
                        .join(" ")
                        .replace(/\*\*/g, "")
                        .replace(/^Advice:\s*/i, "")
                        .trim();
                    break;
            }
        });

        // Optional "Other possible conditions" line
        var otherLine = lines.find(function (l) {
            return l.indexOf("📌") !== -1 || l.indexOf("Other possible conditions") !== -1;
        });
        if (otherLine) {
            var names = otherLine.replace(/^\s*📌\s*/, "").split(":");
            if (names.length > 1) {
                result.other = names[1]
                    .split(",")
                    .map(function (s) { return s.replace(/\.+$/g, "").trim(); })
                    .filter(Boolean);
            }
        }

        return result;
    }

    function isDiagnosisFormat(text) {
        return (
            text.indexOf("Based on the symptoms") !== -1 &&
            /Ayurvedic Medicines/i.test(text) &&
            /Allopathic Medicines/i.test(text)
        );
    }

    function renderDiagnosisCard(parsed, timestamp) {
        var wrapper = makeMessage(false, timestamp);

        var bubble = document.createElement("div");
        bubble.className = "message-bubble";

        var card = document.createElement("div");
        card.className = "diagnosis-card";

        bubble.appendChild(card);
        wrapper.insertBefore(bubble, wrapper.firstChild);

        var blocks = [];

        // Head
        var head = document.createElement("div");
        head.className = "diagnosis-head";
        var eyebrow = document.createElement("div");
        eyebrow.className = "diagnosis-eyebrow";
        eyebrow.textContent = "Likely condition";
        var condition = document.createElement("div");
        condition.className = "diagnosis-condition";
        condition.textContent = parsed.disease || "…";
        head.appendChild(eyebrow);
        head.appendChild(condition);
        blocks.push(head);

        // Ayurvedic section
        if (parsed.ayurvedic.length) {
            blocks.push(makeSection("Ayurvedic Medicines", "diagnosis-label--ayurvedic", parsed.ayurvedic));
        }

        // Allopathic section
        if (parsed.allopathic.length) {
            blocks.push(makeSection("Allopathic Medicines", "diagnosis-label--allopathic", parsed.allopathic));
        }

        // Advice section
        if (parsed.advice) {
            blocks.push(makeSection("Advice", "diagnosis-label--advice", null, parsed.advice));
        }

        // Other possible conditions
        if (parsed.other.length) {
            var other = document.createElement("div");
            other.className = "diagnosis-other";
            other.textContent = "Other possible conditions to consider: " + parsed.other.join(", ") + ".";
            blocks.push(other);
        }

        // Department section
        if (parsed.department) {
            var deptSec = document.createElement("div");
            deptSec.className = "diagnosis-section";
            var deptLabel = document.createElement("div");
            deptLabel.className = "diagnosis-label diagnosis-label--dept";
            deptLabel.textContent = "Recommended Department";
            var deptTag = document.createElement("span");
            deptTag.className = "diagnosis-dept-tag";
            deptTag.textContent = parsed.department;
            deptSec.appendChild(deptLabel);
            deptSec.appendChild(deptTag);
            blocks.push(deptSec);
        }

        // Footer note
        if (parsed.foot) {
            var foot = document.createElement("div");
            foot.className = "diagnosis-foot";
            var footText = document.createElement("p");
            footText.className = "diagnosis-text";
            footText.textContent = parsed.foot;
            foot.appendChild(footText);
            blocks.push(foot);
        }

        // Reveal the card part by part, like a streaming diagnosis.
        setTimeout(function reveal() {
            if (!blocks.length) {
                scrollToBottom();
                return;
            }
            card.appendChild(blocks.shift());
            scrollToBottom();
            setTimeout(reveal, 420 + Math.random() * 260);
        }, 250);
    }

    function makeSection(labelText, modifierClass, items, plainText) {
        var section = document.createElement("div");
        section.className = "diagnosis-section";

        var label = document.createElement("div");
        label.className = "diagnosis-label " + modifierClass;
        label.textContent = labelText;
        section.appendChild(label);

        if (items && items.length) {
            var ul = document.createElement("ul");
            ul.className = "diagnosis-list";
            items.forEach(function (item) {
                var li = document.createElement("li");
                li.textContent = item;
                ul.appendChild(li);
            });
            section.appendChild(ul);
        } else if (plainText) {
            var p = document.createElement("p");
            p.className = "diagnosis-text";
            p.textContent = plainText;
            section.appendChild(p);
        }

        return section;
    }

    // ----------------------------------------------------------
    // RENDERING — plain text / notice bubble
    // ----------------------------------------------------------

    function renderNotice(text, timestamp) {
        var wrapper = makeMessage(false, timestamp);
        var bubble = document.createElement("div");
        bubble.className = "message-bubble bot-bubble notice";
        wrapper.insertBefore(bubble, wrapper.firstChild);
        scrollToBottom();
        typeReveal(bubble, text);
    }

    function typeReveal(container, text) {
        var tokens = [];
        var parts = String(text).split(/\*\*(.+?)\*\*/g);
        for (var k = 0; k < parts.length; k++) {
            if (!parts[k]) continue;
            tokens.push({ bold: k % 2 === 1, chars: Array.from(parts[k]) });
        }

        var total = tokens.reduce(function (n, t) { return n + t.chars.length; }, 0);
        container.innerHTML = "";

        var pos = 0;
        var timer = setInterval(function () {
            var remaining = pos;
            for (var i = 0; i < tokens.length; i++) {
                var t = tokens[i];
                if (remaining >= t.chars.length) {
                    remaining -= t.chars.length;
                    continue;
                }
                var span = document.createElement("span");
                if (t.bold) {
                    var strong = document.createElement("strong");
                    strong.textContent = t.chars[remaining];
                    span.appendChild(strong);
                } else {
                    span.textContent = t.chars[remaining];
                }
                container.appendChild(span);
                break;
            }
            pos++;
            scrollToBottom();
            if (pos >= total) {
                clearInterval(timer);
                container.classList.add("typed");
            }
        }, 14);
    }

    function renderBotResponse(text, timestamp) {
        hideStatusBar();
        if (isDiagnosisFormat(text)) {
            renderDiagnosisCard(parseDiagnosis(text), timestamp);
        } else {
            renderNotice(text, timestamp);
        }
    }

    // ----------------------------------------------------------
    // Network
    // ----------------------------------------------------------

    function sendMessage(text) {
        if (!text) return;

        addUserMessage(text);
        hideStatusBar();
        setBusy(true);

        var typing = addTypingIndicator();

        fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: text })
        })
            .then(function (res) {
                return res.json().then(function (data) {
                    return { ok: res.ok, data: data };
                });
            })
            .then(function (res) {
                if (!res.ok || !res.data.response) {
                    removeNode(typing);
                    renderNotice(
                        "Sorry, something went wrong: " + (res.data.details || res.data.error || "unknown error"),
                        null
                    );
                    return;
                }
                // Let the typing indicator "think" before answering.
                var thinkTime = 1100 + Math.random() * 1200;
                setTimeout(function () {
                    removeNode(typing);
                    renderBotResponse(res.data.response, res.data.timestamp);
                }, thinkTime);
            })
            .catch(function () {
                removeNode(typing);
                renderNotice("Couldn't reach the server. Is the Flask app running on port 5001?", null);
            })
            .finally(function () {
                setBusy(false);
            });
    }

    function removeNode(node) {
        if (!node) return;
        if (node._typingTimer) clearInterval(node._typingTimer);
        if (node.parentNode) {
            node.parentNode.removeChild(node);
        }
    }

    function setBusy(busy) {
        sendBtn.disabled = busy;
        userInput.disabled = busy;
    }

    function handleSubmit() {
        var text = userInput.value.trim();
        if (!text) return;
        userInput.value = "";
        sendMessage(text);
        userInput.focus();
    }

    // ----------------------------------------------------------
    // Status bar (initial connection check)
    // ----------------------------------------------------------

    function setStatus(text, isError) {
        if (!statusBar) return;
        var label = statusBar.querySelector(".status-text");
        if (label) label.textContent = text;
        statusBar.classList.toggle("error", !!isError);
    }

    function checkHealth() {
        fetch("/health", { method: "GET" })
            .then(function (res) { return res.ok ? res.json() : Promise.reject(); })
            .then(function (data) {
                setStatus("online — " + (data.diseases_loaded || 0) + " conditions indexed");
            })
            .catch(function () {
                setStatus("offline — server not responding", true);
            });
    }

    // ----------------------------------------------------------
    // Voice input (Web Speech API, where supported)
    // ----------------------------------------------------------

    var recognition = null;
    var listening = false;

    function startListening() {
        var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!SR) {
            renderNotice("Voice input isn't supported by this browser. Please type your symptoms instead.", null);
            return;
        }

        if (!recognition) {
            recognition = new SR();
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = "en-IN";

            recognition.onresult = function (event) {
                var transcript = "";
                for (var i = 0; i < event.results.length; i++) {
                    transcript += event.results[i][0].transcript;
                }
                var text = transcript.trim();
                if (text) {
                    userInput.value = text;
                    sendMessage(text);
                }
            };

            recognition.onerror = function (event) {
                if (event.error !== "no-speech" && event.error !== "aborted") {
                    renderNotice("Microphone error: " + event.error, null);
                }
            };

            recognition.onend = function () {
                listening = false;
                micBtn.classList.remove("listening");
                micBtn.title = "Click to speak";
            };
        }

        listening = true;
        micBtn.classList.add("listening");
        micBtn.title = "Listening…";
        try {
            recognition.start();
        } catch (e) {
            /* already started */
        }
    }

    // ----------------------------------------------------------
    // Wire up events
    // ----------------------------------------------------------

    sendBtn.addEventListener("click", handleSubmit);
    userInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            handleSubmit();
        }
    });
    micBtn.addEventListener("click", startListening);

    // On load
    if (welcomeTime) welcomeTime.textContent = nowLabel();
    checkHealth();
    userInput.focus();
})();