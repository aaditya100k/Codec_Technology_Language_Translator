document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('translator-form');
  const sourceInput = document.getElementById('source-text');
  const targetInput = document.getElementById('target-text');
  const sourceSelect = document.getElementById('source-language');
  const targetSelect = document.getElementById('target-language');
  const sourceCount = document.getElementById('source-count');
  const statusMessage = document.getElementById('status-message');
  const swapButton = document.getElementById('swap-languages');

  if (sourceInput && sourceCount) {
    sourceInput.addEventListener('input', () => {
      sourceCount.textContent = `${sourceInput.value.length}/2000`;
    });
  }

  if (form) {
    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      const payload = {
        text: sourceInput?.value || '',
        source_language: sourceSelect?.value || 'auto',
        target_language: targetSelect?.value || 'en'
      };

      try {
        const response = await fetch('/api/translate', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        const data = await response.json();
        if (targetInput) {
          targetInput.value = data.translated_text || '';
        }
        if (statusMessage) {
          statusMessage.textContent = data.message || 'Translation complete.';
        }
      } catch (error) {
        if (statusMessage) {
          statusMessage.textContent = 'Unable to translate right now.';
        }  
      }
    });
  }

  if (swapButton && sourceSelect && targetSelect) {
    swapButton.addEventListener('click', () => {
      const sourceValue = sourceSelect.value;
      const targetValue = targetSelect.value;
      sourceSelect.value = targetValue;
      targetSelect.value = sourceValue;
      const temp = sourceInput.value;
      sourceInput.value = targetInput.value;
      targetInput.value = temp;
      if (sourceCount) sourceCount.textContent = `${sourceInput.value.length}/2000`;
    });
  }

  document.querySelectorAll('.copy-btn').forEach((button) => {
    button.addEventListener('click', async () => {
      const targetId = button.getAttribute('data-target');
      const target = document.getElementById(targetId);
      if (target) {
        await navigator.clipboard.writeText(target.value || target.textContent || '');
      }
    });
  });

  document.querySelectorAll('.speak-btn').forEach((button) => {
    button.addEventListener('click', () => {
      const targetId = button.getAttribute('data-target');
      const target = document.getElementById(targetId);
      const lang = button.getAttribute('data-language') || 'en';
      const utterance = new SpeechSynthesisUtterance(target?.value || target?.textContent || '');
      utterance.lang = lang;
      window.speechSynthesis.cancel();
      window.speechSynthesis.speak(utterance);
    });
  });
});
