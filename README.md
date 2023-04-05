# Hymnal

Just a hymnal.

---

> **Error Note** : If you face such an error:

```console
$ pnpm build

> hymnal@0.1.0 build /home/user/myproject
> vite build

vite v4.2.1 building for production...
transforming (1) index.htmlerror TS5104: Option 'isolatedModules' is redundant and cannot be specified with option 'verbatimModuleSyntax'.

✓ 3 modules transformed.
9:45:35 am [vite-plugin-svelte] dom compile done.
package files   time    avg
✓ built in 923ms
[vite-plugin-svelte] Error while preprocessing /home/user/myproject/src/App.svelte - [svelte-preprocess] Encountered type error
file: /home/user/myproject/src/App.svelte
error during build:
Error: Error while preprocessing /home/user/myproject/src/App.svelte - [svelte-preprocess] Encountered type error
    at throwError (/home/user/myproject/node_modules/.pnpm/svelte-preprocess@5.0.3_postcss-load-config@4.0.1_postcss@8.4.21_svelte@3.58.0_typescript@5.0.3/node_modules/svelte-preprocess/dist/modules/errors.js:5:11)
    at throwTypescriptError (/home/user/myproject/node_modules/.pnpm/svelte-preprocess@5.0.3_postcss-load-config@4.0.1_postcss@8.4.21_svelte@3.58.0_typescript@5.0.3/node_modules/svelte-preprocess/dist/modules/errors.js:9:28)
    at transpileTs (/home/user/myproject/node_modules/.pnpm/svelte-preprocess@5.0.3_postcss-load-config@4.0.1_postcss@8.4.21_svelte@3.58.0_typescript@5.0.3/node_modules/svelte-preprocess/dist/transformers/typescript.js:209:47)
    at simpleTranspiler (/home/user/myproject/node_modules/.pnpm/svelte-preprocess@5.0.3_postcss-load-config@4.0.1_postcss@8.4.21_svelte@3.58.0_typescript@5.0.3/node_modules/svelte-preprocess/dist/transformers/typescript.js:300:60)
    at transformer (/home/user/myproject/node_modules/.pnpm/svelte-preprocess@5.0.3_postcss-load-config@4.0.1_postcss@8.4.21_svelte@3.58.0_typescript@5.0.3/node_modules/svelte-preprocess/dist/transformers/typescript.js:345:11)
    at transform (/home/user/myproject/node_modules/.pnpm/svelte-preprocess@5.0.3_postcss-load-config@4.0.1_postcss@8.4.21_svelte@3.58.0_typescript@5.0.3/node_modules/svelte-preprocess/dist/autoProcess.js:46:12)
    at process.processTicksAndRejections (node:internal/process/task_queues:95:5)
    at async /home/user/myproject/node_modules/.pnpm/svelte-preprocess@5.0.3_postcss-load-config@4.0.1_postcss@8.4.21_svelte@3.58.0_typescript@5.0.3/node_modules/svelte-preprocess/dist/autoProcess.js:117:29
    at async script (/home/user/myproject/node_modules/.pnpm/svelte-preprocess@5.0.3_postcss-load-config@4.0.1_postcss@8.4.21_svelte@3.58.0_typescript@5.0.3/node_modules/svelte-preprocess/dist/autoProcess.js:147:33)
    at async process_single_tag (file:///home/user/myproject/node_modules/.pnpm/svelte@3.58.0/node_modules/svelte/compiler.mjs:44016:27)
 ELIFECYCLE  Command failed with exit code 1.
```

Make the following change in `tsconfig.json`

```diff
-"isolatedModules": true
+"verbatimModuleSyntax": true
```
