// node render.cjs daftar.json  -> tiap butir {html, pdf, margin:[t,r,b,l]} dirender tanpa header/footer
const { chromium } = require('playwright');
const jobs = JSON.parse(require('fs').readFileSync(process.argv[2], 'utf8'));
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const j of jobs) {
    await p.goto('file://' + j.html, { waitUntil: 'load' });
    const [t, r, bo, l] = j.margin || ['22mm', '18mm', '19mm', '18mm'];
    await p.pdf({ path: j.pdf, format: 'A4', printBackground: true, displayHeaderFooter: false,
      margin: { top: t, right: r, bottom: bo, left: l } });
    console.log('ok', j.pdf.split('/').pop());
  }
  await b.close();
})();
