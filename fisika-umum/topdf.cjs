const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + process.argv[2], { waitUntil: 'load' });
  const t = process.argv[4] || '';
  await p.pdf({ path: process.argv[3], format: 'A4', printBackground: true, displayHeaderFooter: true,
    headerTemplate: `<div style="font-family:Inter,sans-serif;font-size:7px;letter-spacing:1.5px;color:#1b75bc;font-weight:600;width:100%;padding:0 18mm;text-transform:uppercase">${t}</div>`,
    footerTemplate: '<div style="font-family:Inter,sans-serif;font-size:8.5px;color:#17355e;font-weight:700;width:100%;text-align:center"><span class="pageNumber"></span></div>',
    margin: { top: '20mm', bottom: '18mm', left: '20mm', right: '20mm' } });
  await b.close(); })();
