async function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value;
    if (!message) return;

    appendMessage("you", message);
    input.value = "";

    // Typing indicator
    let typingElem = appendMessage("typing", "Agent is typing...");

    let response = await fetch("/send/", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: message})
    });

    let data = await response.json();
    typingElem.remove();
    appendMessage(data.agent, data.response);
}

function appendMessage(role, text) {
    let chatBox = document.getElementById("chat-box");
    let div = document.createElement("div");
    div.classList.add("message");
    div.classList.add(role);
    div.innerText = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
    return div;
}
