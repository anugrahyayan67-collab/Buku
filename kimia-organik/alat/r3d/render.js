// pakai: node render.js daftar.json  (daftar: [{spec, out}])
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const b = await chromium.launch({args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--allow-file-access-from-files']});
  const pg = await b.newPage(); await pg.goto('file://' + path.join(__dirname, 'render.html')); await pg.waitForFunction('window.siap === true');
  const meta = {};
  for (const j of jobs) {
    const r = await pg.evaluate(s => window.render(s), j.spec);
    fs.writeFileSync(j.out, Buffer.from(r.png.split(',')[1], 'base64')); meta[j.out] = r.proj;
  }
  fs.writeFileSync(process.argv[2].replace(/\.json$/, '.meta.json'), JSON.stringify(meta));
  await b.close();
})();
