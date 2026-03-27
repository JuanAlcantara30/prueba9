function toggleAgent() {
    const window = document.getElementById('agent-window');
    window.style.display = window.style.display === 'flex' ? 'none' : 'flex';
}

function sendAgentMessage() {
    const input = document.getElementById('agent-input');
    const container = document.getElementById('agent-messages');
    
    if (!input.value.trim()) return;

    // User message
    const div = document.createElement('div');
    div.className = 'chat-bubble';
    div.style.alignSelf = 'flex-end';
    div.style.background = '#dcf8c6';
    div.style.marginLeft = 'auto';
    div.textContent = input.value;
    container.appendChild(div);
    
    const userText = input.value.toLowerCase();
    input.value = '';
    
    // Bot Response simulation
    setTimeout(() => {
        const botDiv = document.createElement('div');
        botDiv.className = 'chat-bubble bot';
        
        if (userText.includes('hola') || userText.includes('buenos')) {
            botDiv.textContent = '¡Hola! Dra. Sabrinsky Flores te saluda. ¿En qué podemos ayudarte hoy?';
        } else if (userText.includes('cita') || userText.includes('agenda')) {
            botDiv.textContent = 'Perfecto, para agendar necesitamos tu nombre y el servicio.';
        } else {
            botDiv.textContent = 'Estamos procesando tu solicitud. Un asesor se comunicará contigo vía WhatsApp en breve.';
        }
        
        container.appendChild(botDiv);
        container.scrollTop = container.scrollHeight;
    }, 1000);
}
