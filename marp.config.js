module.exports = {
  // テーマ設定
  themeSet: './themes',

  // Markdownの設定
  engine: {
    markdown: 'markdown-it',
    options: {
      html: true,
      breaks: true,
      linkify: true,
    },
  },

  // mermaidプラグインの有効化
  mermaid: {
    // mermaidのテーマ設定（オプション）
    theme: 'default',
  },
  
  // HTMLでmermaidを処理するための設定
  html: true,
  
  // 追加のプラグイン
  // mermaid-plugin をインストールしておく必要があります
  plugins: [
    'marp-engine-mermaid',
  ],
}; 