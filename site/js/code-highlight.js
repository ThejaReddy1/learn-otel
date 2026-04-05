/* ============================================
   code-highlight.js — Lightweight syntax highlighting
   for Python, YAML, PowerShell, and JSON
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.code-block pre code').forEach(block => {
    const lang = block.closest('.code-block').dataset.lang || '';
    block.innerHTML = highlightCode(block.textContent, lang);
  });
});

function highlightCode(code, lang) {
  // Escape HTML first
  code = code
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');

  if (lang === 'python' || lang === 'py') {
    code = highlightPython(code);
  } else if (lang === 'yaml' || lang === 'yml') {
    code = highlightYaml(code);
  } else if (lang === 'powershell' || lang === 'shell' || lang === 'bash') {
    code = highlightShell(code);
  } else if (lang === 'json') {
    code = highlightJson(code);
  }
  
  // Safe flip to real HTML tokens at the very end to avoid regex collisions
  code = code.replace(/~S~([a-z-]+)~/g, '<span class="token-$1">');
  code = code.replace(/~E~/g, '</span>');
  return code;
}

function highlightPython(code) {
  // Order matters: comments first, then strings, then keywords, etc.
  
  // Comments
  code = code.replace(/(#.*$)/gm, '~S~comment~$1~E~');
  
  // Triple-quoted strings
  code = code.replace(/("""[\s\S]*?"""|'''[\s\S]*?''')/g, '~S~string~$1~E~');
  
  // Strings (double and single)
  // We use negative lookbehind/lookahead ideally, but sticking to simple regex:
  code = code.replace(/("(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*')/g, '~S~string~$1~E~');
  
  // Decorators
  code = code.replace(/(@[\w.]+)/g, '~S~decorator~$1~E~');
  
  // Keywords
  const kwds = ['def','class','import','from','return','if','elif','else','for','while',
    'with','as','try','except','finally','raise','pass','break','continue',
    'and','or','not','in','is','None','True','False','lambda','yield','async','await',
    'print','self','__name__','__main__'];
  const kwdRe = new RegExp('\\b(' + kwds.join('|') + ')\\b', 'g');
  code = code.replace(kwdRe, '~S~keyword~$1~E~');
  
  // Built-in functions
  const builtins = ['print','len','range','int','str','float','list','dict','set','tuple',
    'type','isinstance','enumerate','zip','map','filter','open','super'];
  const builtinRe = new RegExp('\\b(' + builtins.join('|') + ')(?=\\()', 'g');
  code = code.replace(builtinRe, '~S~builtin~$1~E~');
  
  // Numbers
  code = code.replace(/\b(\d+\.?\d*)\b/g, '~S~number~$1~E~');
  
  // Function definitions
  code = code.replace(/\b(def\s+)(\w+)/g, '$1~S~function~$2~E~');
  
  return code;
}

function highlightYaml(code) {
  // Comments
  code = code.replace(/(#.*$)/gm, '~S~comment~$1~E~');
  
  // Keys  
  code = code.replace(/^(\s*)([\w.-]+)(\s*:)/gm, '$1~S~keyword~$2~E~$3');
  
  // Strings
  code = code.replace(/("(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*')/g, '~S~string~$1~E~');
  
  // Numbers
  code = code.replace(/:\s*(\d+)/g, ': ~S~number~$1~E~');
  
  return code;
}

function highlightShell(code) {
  // Comments
  code = code.replace(/(#.*$)/gm, '~S~comment~$1~E~');
  
  // Strings
  code = code.replace(/("(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*')/g, '~S~string~$1~E~');
  
  // Commands / keywords
  const cmds = ['py','python','python3','pip','docker','docker-compose','npm','npx',
    'cd','mkdir','ls','cat','echo','curl','git','install','compose','run','up'];
  const cmdRe = new RegExp('\\b(' + cmds.join('|') + ')\\b', 'g');
  code = code.replace(cmdRe, '~S~keyword~$1~E~');
  
  // Flags
  code = code.replace(/(\s)(--?[\w-]+)/g, '$1~S~function~$2~E~');
  
  return code;
}

function highlightJson(code) {
  // Strings (keys and values)
  code = code.replace(/("(?:[^"\\]|\\.)*")\s*:/g, '~S~keyword~$1~E~:');
  code = code.replace(/:\s*("(?:[^"\\]|\\.)*")/g, ': ~S~string~$1~E~');
  
  // Numbers
  code = code.replace(/:\s*(\d+\.?\d*)/g, ': ~S~number~$1~E~');
  
  // Booleans and null
  code = code.replace(/\b(true|false|null)\b/g, '~S~keyword~$1~E~');
  
  return code;
}
