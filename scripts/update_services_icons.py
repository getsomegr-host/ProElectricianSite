import re

# mapping of services to emojis
emoji_map = {
    'Residential Electrical': '🏠',
    'Commercial Electrical': '🏢',
    'Electrical Safety Inspections': '🛡️',
    'Emergency Electrical Services': '⚡',
    'Home EV Charger Installation': '🔌',
    'Backup Generator Services': '🔋',
    '24‑Hour Electrical Service': '🕒',
    'Professional Electrical Troubleshooting': '🔍',
    'Electrical Panel Evaluations': '📊',
    'Amperage Issue Resolution': '⚡',
    'Range, Dryer & AC Outlet Installation': '🔌',
    'Electrical Code Violation Corrections': '⚠️',
    'Indoor & Outdoor Lighting': '💡',
    'Circuit Breaker Repair & Upgrades': '🔩',
    'Communication & Data Line Installation': '📡',
    'Custom Lighting Design': '🎨',
    'Dedicated Circuits': '🔌',
    'Dimming & Flickering Light Fixes': '💡',
    'Energy‑Saving Lighting Options': '🌱',
    'Hot Tub & Pool Wiring': '🏊',
    'Ceiling & Attic Fan Install/Repair': '🌀',
    'Lighting Safety Recommendations': '🛡️',
    'Motion Sensors & Exterior Lighting': '🚨',
    'Outlets & Specialty Receptacles': '🔌',
    'Power Consumption Meters': '📈',
    'Power Outage Solutions': '⚡',
    'Recessed Lighting Installation': '💡',
    'Light Bulb & Ballast Replacement': '💡',
    'Smart Lighting Systems': '📱',
    'Smoke & Carbon Monoxide Detectors': '🚨',
    'Transfer Switch Installation': '🔁',
    'Transformer Inspection & Testing': '🔧',
    'Transformer Installation': '⚙️',
    'Whole-House Surge Protector Installation': '🌩️',
}

# read html
path = r'c:/Users/tmill/OneDrive/Documents/ProElectric/ProElectricianSite/index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# find current service list block
match = re.search(r'(<div class="service-list" role="list">)(.*?)(</div>)', html, re.DOTALL)
if not match:
    print('service list not found')
    sys.exit(1)

services_html = match.group(2)

# build new block by iterating over articles
articles = re.findall(r'<article class="service" role="listitem">(.*?)</article>', services_html, re.DOTALL)
new_articles = []
for art in articles:
    # find title and description
    h3 = re.search(r'<h3>(.*?)</h3>', art)
    p = re.search(r'<p>(.*?)</p>', art, re.DOTALL)
    if not h3 or not p:
        continue
    title = h3.group(1).strip()
    desc = p.group(1).strip()
    emoji = emoji_map.get(title, '⚡')
    svg = f'<svg class="service-icon" viewBox="0 0 24 24"><text x="12" y="16" font-size="14" text-anchor="middle">{emoji}</text></svg>'
    new_art = f'    <article class="service" role="listitem">\n      {svg}\n      <h3>{title}</h3>\n      <p>{desc}</p>\n    </article>'
    new_articles.append(new_art)

new_div = match.group(1) + '\n' + '\n'.join(new_articles) + '\n  ' + match.group(3)

new_html = html[:match.start()] + new_div + html[match.end():]
with open(path, 'w', encoding='utf-8') as f:
    f.write(new_html)
print('Updated service icons to emojis')
