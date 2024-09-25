import globals from 'globals';
import pluginJs from '@eslint/js';
import tseslint from 'typescript-eslint';
import pluginVue from 'eslint-plugin-vue';

export default [
  {files: ['**/*.{js,mjs,cjs,ts,vue}']},
  {languageOptions: { globals: globals.browser }},
  pluginJs.configs.recommended,
  ...tseslint.configs.recommended,
  ...pluginVue.configs['flat/essential'],
  {files: ['**/*.vue'], languageOptions: {parserOptions: {parser: tseslint.parser}}},
  {
    rules: {
      'quotes': ['error', 'single'],
      'semi': ['error', 'always'],
      'no-console': 'warn',
      'no-unused-vars': ['warn', { 'argsIgnorePattern': '^_' }],
      'vue/no-unused-vars': 'warn',
      'vue/singleline-html-element-content-newline': 'off',
    },
  },
];
