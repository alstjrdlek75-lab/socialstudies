import re

with open('/Users/mac/.gemini/antigravity/scratch/edurecall/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix sanitizeAndNormalizeGroupHeaders
old_sanitize = """
            const txt = node.textContent.trim();
            if (txt) {
"""

new_sanitize = """
            const txt = node.textContent.trim();
            if (txt && txt !== 'visibility') {
"""

if old_sanitize in text:
    text = text.replace(old_sanitize, new_sanitize)
    print("Fixed sanitizeAndNormalizeGroupHeaders")
else:
    print("Could not find sanitize block")

# 2. Add cleanup during renderTopic
old_render = """
        if (customHtml) {
          subnoteContainer.innerHTML = customHtml;
          if (btnResetCustomTape) btnResetCustomTape.classList.remove('hidden');
        } else {
          subnoteContainer.innerHTML = topic.contentHtml;
          if (btnResetCustomTape) btnResetCustomTape.classList.add('hidden');
        }
"""

new_render = """
        if (customHtml) {
          subnoteContainer.innerHTML = customHtml;
          if (btnResetCustomTape) btnResetCustomTape.classList.remove('hidden');
        } else {
          subnoteContainer.innerHTML = topic.contentHtml;
          if (btnResetCustomTape) btnResetCustomTape.classList.add('hidden');
        }

        // --- Cleanup stray 'visibility' strings from previous bugs ---
        subnoteContainer.querySelectorAll('.font-bold').forEach(fontBold => {
          fontBold.querySelectorAll('span').forEach(s => {
            if (s.textContent && s.textContent.endsWith('visibility')) {
               s.textContent = s.textContent.replace(/visibility$/, '').trim();
            }
          });
          // Also check text nodes directly inside fontBold
          Array.from(fontBold.childNodes).forEach(node => {
            if (node.nodeType === Node.TEXT_NODE && node.textContent.includes('visibility')) {
              node.textContent = node.textContent.replace(/visibility/g, '').trim();
            }
          });
        });
        // -----------------------------------------------------------
"""

if old_render in text:
    text = text.replace(old_render, new_render)
    print("Added cleanup logic in renderTopic")
else:
    print("Could not find renderTopic block")


with open('/Users/mac/.gemini/antigravity/scratch/edurecall/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

