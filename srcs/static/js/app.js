function startChat(userId) {
    document.getElementById('recipient_id').value = userId;
    // Optionnel : scroll vers la zone de message
    document.querySelector('.messages-container').scrollIntoView();
}