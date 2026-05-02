function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showNotification('Ссылка скопирована!', 'success');
    }).catch(() => {
        showNotification('Не удалось скопировать', 'error');
    });
}

function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type}`;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1000;
        animation: slideIn 0.3s ease;
    `;
    notification.innerHTML = `<span>${type === 'success' ? '✅' : '❌'}</span><span>${message}</span>`;
    document.body.appendChild(notification);

    setTimeout(() => {
        notification.style.opacity = '0';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

document.addEventListener('DOMContentLoaded', function () {
    const gameCards = document.querySelectorAll('.game-card, .game-row');
    gameCards.forEach(card => {
        card.addEventListener('click', function () {
            const urlElement = this.querySelector('.game-url, .game-detail');
            if (urlElement) {
                copyToClipboard(urlElement.textContent);
            }
        });
    });

    const deleteForm = document.querySelector('form[method="post"] input[name="name"]');
    if (deleteForm) {
        deleteForm.closest('form').addEventListener('submit', function (e) {
            const gameName = deleteForm.value;
            if (!confirm(`Вы уверены, что хотите удалить игру "${gameName}"?`)) {
                e.preventDefault();
            }
        });
    }

    console.log('SteamPrice JS загружен');
});