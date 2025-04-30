async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (!message) return;

  addMessage("You: " + message, "user");

  const response = await fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  });

  const data = await response.json();
  addMessage("Assistant: " + data.response, "bot");

  input.value = "";
}

function addMessage(msg, type) {
  const box = document.getElementById("chat-box");
  const div = document.createElement("div");
  div.className = "chat-message " + type;
  div.innerText = msg;
  box.appendChild(div);
  box.scrollTop = box.scrollHeight;
}

  