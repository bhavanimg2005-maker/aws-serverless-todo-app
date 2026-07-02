// Replace this with your API Gateway URL
const apiUrl = "YOUR_API_GATEWAY_URL/tasks";

async function loadTasks() {
    const response = await fetch(apiUrl);
    const data = await response.json();

    const list = document.getElementById("taskList");
    list.innerHTML = "";

    data.forEach(task => {
        const li = document.createElement("li");
        li.innerText = task.task;
        list.appendChild(li);
    });
}

async function addTask() {
    const task = document.getElementById("taskInput").value;

    await fetch(apiUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ task })
    });

    document.getElementById("taskInput").value = "";
    loadTasks();
}

loadTasks();
