document.addEventListener('DOMContentLoaded', () => {
  const toast = document.getElementById('toast');
  const modal = document.getElementById('palette-modal');
  const closeModal = document.getElementById('close-modal');
  const modalTitle = document.getElementById('modal-title');
  const largeContainer = document.getElementById('large-palette-container');
  const refreshBtn = document.getElementById('refresh-btn');

  let currentColors = []; // Guarda los colores de la paleta actualmente abierta

  function showToast(message) {
    toast.textContent = message;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 2500);
  }

  function openModal(colors, title) {
    currentColors = colors;
    modalTitle.textContent = title;
    largeContainer.innerHTML = '';

    colors.forEach(color => {
      const block = document.createElement('div');
      block.className = 'large-color-block';
      block.style.backgroundColor = color;
      block.setAttribute('data-color', color);

      const hex = document.createElement('span');
      hex.className = 'hex-code';
      hex.textContent = color;

      block.appendChild(hex);
      largeContainer.appendChild(block);

      block.addEventListener('click', () => {
        navigator.clipboard.writeText(color).then(() => {
          showToast(`¡${color} copiado!`);
        });
      });
    });

    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  closeModal.addEventListener('click', () => {
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
  });

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.classList.remove('active');
      document.body.style.overflow = 'auto';
    }
  });

  function setupTriggers() {
    document.querySelectorAll('.palette-trigger').forEach(card => {
      const newCard = card.cloneNode(true);
      card.parentNode.replaceChild(newCard, card);

      newCard.addEventListener('click', () => {
        const colors = JSON.parse(newCard.getAttribute('data-colors'));
        const title = newCard.getAttribute('data-title');
        openModal(colors, title);
      });
    });
  }

  setupTriggers();

  document.querySelectorAll('.export-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const format = btn.getAttribute('data-format');
      let output = '';

      if (format === 'css') {
        output = ':root {\n';
        currentColors.forEach((color, i) => {
          output += `  --color-${i + 1}: ${color};\n`;
        });
        output += '}';
      } else if (format === 'scss') {
        currentColors.forEach((color, i) => {
          output += `$color-${i + 1}: ${color};\n`;
        });
      } else if (format === 'json') {
        output = JSON.stringify(currentColors, null, 2);
      }

      navigator.clipboard.writeText(output).then(() => {
        showToast(`Formato ${format.toUpperCase()} copiado`);
      });
    });
  });

  refreshBtn.addEventListener('click', () => {
    refreshBtn.classList.add('loading');
    setTimeout(() => {
      window.location.reload();
    }, 600);
  });
});
