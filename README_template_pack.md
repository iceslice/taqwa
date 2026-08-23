# Taqwa Global Education — Template Pack

Drop this into your `taqwa` project (merge, don't overwrite `manage.py` etc.):

```
static/css/main.css        → static/css/main.css
static/css/rtl.css         → static/css/rtl.css
templates/                 → templates/  (base.html, partials/, core/, services/, universities/, leads/, portal/)
leads/templatetags/        → leads/templatetags/   (new folder inside your existing leads app)
```

## Design direction
Deep jade-teal + warm gold on a cool paper background, with a recurring
"route line" / boarding-pass motif (dotted flight path, perforated stat
cards) — a literal nod to what the business does: move a student from
where they are to an offer letter and a visa. Fonts are Fraunces (display)
and Inter (body), with Noto Serif/Sans Bengali, Noto Naskh/Sans Arabic and
Noto Sans SC stacked into the same declarations so headings and body text
render correctly no matter which of the 10 languages is active — the
browser auto-picks the right font per character.

## Two things to add to `config/settings.py`

**1. `widget_tweaks` app** (used in `leads/capture_form.html`):
```python
INSTALLED_APPS = [
    ...
    "widget_tweaks",
]
```
(You already installed the package in requirements.txt — this just registers it.)

**2. A context processor so `WHATSAPP_NUMBER` and `site` are available on every page**, not just the homepage. Add this to `core/context_processors.py` (new file):

```python
from .models import SiteSettings
from django.conf import settings

def site_settings(request):
    obj, _ = SiteSettings.objects.get_or_create(pk=1)
    return {
        "site": obj,
        "WHATSAPP_NUMBER": settings.WHATSAPP_NUMBER,
    }
```

Then register it in `TEMPLATES` → `OPTIONS` → `context_processors` in `config/settings.py`:
```python
"context_processors": [
    ...
    "core.context_processors.site_settings",
],
```
Without this, `home.html` still works (its view passes `site` explicitly), but the WhatsApp floating button and footer contact info on *other* pages (services, universities, portal, etc.) will silently fall back to the defaults baked into the templates.

## Seed data to add in `/admin/` before it looks "real"

- `core.StaticPage`: create one with `slug="about"` — the nav's About link depends on it.
- A few `services.Service` rows (so the homepage/services grid isn't empty).
- A `universities.Country` + a few `universities.University` rows.
- `portal.DocumentType` rows — Passport Copy, Academic Transcripts, IELTS/TOEFL Score, Bank Solvency Certificate, SOP, CV, Recommendation Letters, Photo — these drive the student dashboard checklist.

## Notes
- `leads/templatetags/leads_extras.py` adds a `get_item` filter used only
  by the CRM dashboard's pipeline-count chips — Django templates can't
  index a dict by a loop variable without it.
- Run `python manage.py makemessages -l bn -l ar -l ur -l fa -l ms -l fr -l ru -l zh_Hans -l es`
  then translate the generated `.po` files, then `compilemessages`, to
  get non-English UI text — the templates are already wrapped in
  `{% trans %}` / `{% blocktrans %}` throughout.
- Static/media files referenced with `{% static %}` need
  `python manage.py collectstatic` in production (already covered in the
  deployment guide).
