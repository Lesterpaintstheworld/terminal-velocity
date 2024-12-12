// WebSocket connection
let ws = new WebSocket(`ws://${window.location.host}/ws`);

function updateConnectionStatus(status) {
    const statusEl = document.getElementById('connection-status');
    statusEl.className = `status-indicator ${status}`;
    statusEl.textContent = status === 'connected' ? 'Connected' : 'Disconnected';
}

ws.onopen = () => updateConnectionStatus('connected');
ws.onclose = () => updateConnectionStatus('disconnected');

ws.onmessage = function(event) {
    const data = JSON.parse(event.data);
    updateAgents(data.agents);
    updateActivity(data.activity);
    updateCommits(data.commits);
};

function updateAgents(agents) {
    const container = document.getElementById('agents-container');
    if (!agents || !agents.length) {
        container.innerHTML = '<div class="info-message">No active agents found</div>';
        return;
    }
    
    container.innerHTML = agents.map(agent => `
        <div class="agent-card">
            <img src="${agent.avatar}" class="agent-avatar" alt="${agent.name}" 
                 onerror="this.src='/static/avatars/default.png'">
            <div class="agent-info">
                <h3>${agent.name}</h3>
                <p class="objective">${agent.objective || 'No objective set'}</p>
                <span class="status-badge ${agent.status}">${agent.status}</span>
            </div>
        </div>
    `).join('');
}

function updateActivity(activities) {
    const container = document.getElementById('activity-container');
    if (!activities || !activities.length) {
        container.innerHTML = '<div class="info-message">No recent activity</div>';
        return;
    }
    
    container.innerHTML = activities.map(activity => `
        <div class="activity-item">
            <div class="timestamp">${activity.timestamp}</div>
            <div class="message">${activity.message}</div>
        </div>
    `).join('');
}

function updateCommits(commits) {
    const container = document.getElementById('commits-container');
    if (!commits || !commits.length) {
        container.innerHTML = '<div class="info-message">No recent commits</div>';
        return;
    }
    
    container.innerHTML = commits.map(commit => `
        <div class="commit-item">
            <div class="timestamp">${commit.hash}</div>
            <div class="message">${commit.message}</div>
        </div>
    `).join('');
}