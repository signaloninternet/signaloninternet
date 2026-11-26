import { readFile, writeFile } from 'node:fs/promises';
import { join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const [renderer, calendarPath] = process.argv.slice(2);
if (!renderer || !calendarPath) {
  throw new Error('Usage: node render_weekly.mjs <github-cool-readme checkout> <calendar JSON>');
}

const upstream = pathToFileURL(resolve(renderer) + '/');
const { weeklyData } = await import(new URL('src/cards/weekly/data.ts', upstream));
const { renderDisplayWeekly } = await import(new URL('src/cards/weekly/display.ts', upstream));
const { look } = await import(new URL('src/display/dmd.ts', upstream));

const calendar = JSON.parse(await readFile(calendarPath, 'utf8'));
const weekly = weeklyData({ snapshot: { calendar } });
const license = await readFile(new URL('LICENSE', upstream), 'utf8');
const credit = '<!-- Animation from https://github.com/pedrocatalao/github-cool-readme (v1.8.1)\n' + license.trimEnd() + '\n-->\n';

for (const [mode, background] of [['light', '#fcf7eb'], ['dark', '#271d16']]) {
  const dark = mode === 'dark';
  const style = {
    look: {
      ...look('amber', mode, dark),
      lit: dark ? '#ffe2bc' : '#58351e',
      accent: dark ? '#ffad62' : '#984f20',
      dim: 0.8,
      unlitOpacity: 0.055,
    },
    dots: true,
    grid: true,
    animations: true,
    background,
  };
  const svg = renderDisplayWeekly(weekly, 'Weekly rhythm', style);
  await writeFile(join('assets', `weekly-${mode}.svg`), credit + svg);
}
