# Builds the playbook HTML (DA + EN + privacy pages) from one data table,
# so the JSON-LD FAQ is always identical to the visible FAQ.
import json, sys, html, os
OUT = sys.argv[1]
BASE = "https://dkkimo1.github.io/claude-playbook"
DATE = "2026-10-20"

SRC = [
 ("https://support.claude.com/en/articles/9266767-what-is-the-team-plan", {"da": "Anthropic: Hvad er Team-planen?", "en": "Anthropic: What is the Team plan?"}),
 ("https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan", {"da": "Anthropic: Hvad er Enterprise-planen?", "en": "Anthropic: What is the Enterprise plan?"}),
 ("https://privacy.claude.com/en/articles/7996862-how-do-i-view-and-sign-your-data-processing-addendum-dpa", {"da": "Anthropic: Databehandleraftalen (DPA)", "en": "Anthropic: The Data Processing Addendum (DPA)"}),
 ("https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training", {"da": "Anthropic: Bruges mine data til træning af modeller?", "en": "Anthropic: Is my data used for model training?"}),
 ("https://support.claude.com/en/articles/9517075-what-are-projects", {"da": "Anthropic: Hvad er projekter?", "en": "Anthropic: What are projects?"}),
 ("https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities", {"da": "Anthropic: Connectors", "en": "Anthropic: Use connectors"}),
 ("https://eur-lex.europa.eu/eli/reg/2024/1689/oj", {"da": "EU's AI-forordning, forordning (EU) 2024/1689", "en": "EU AI Act, Regulation (EU) 2024/1689"}),
]

L = {}
L["da"] = dict(
 lang="da", locale="da_DK", path="", css="style.css", img="img/", sfx="",
 title="AI-implementering med Claude: en åben playbook for virksomheder",
 desc="Sådan får en virksomhed på 5 til 80 ansatte Claude i fast drift: valg af plan, data og GDPR, de første arbejdsgange, oplæring og måling. En gratis playbook i seks trin.",
 og_title="AI-implementering med Claude: en åben playbook",
 og_desc="Seks trin fra første login til målbar effekt. Skrevet til virksomheder på 5 til 80 ansatte.",
 brand="Claude-playbook", nav='<a href="./" aria-current="page">Dansk</a> <a href="en/" hreflang="en">English</a>',
 hero_alt="Seks trin i en AI-implementering med Claude, fra at udpege en ejer til måling, vist som en tidslinje",
 lead="De fleste virksomheder starter med Claude på samme måde. Nogen opretter en konto, et par kolleger prøver det, og tre måneder senere ved ingen, om det har gjort en forskel. Denne playbook er de seks trin, der gør et forsøg til fast drift. Den er skrevet til virksomheder på 5 til 80 ansatte og er gratis at bruge og dele.",
 byline="Udgivet af Brinvik, oktober 2026. Fakta er tjekket mod Anthropics egen dokumentation i oktober 2026. Kilderne står nederst.",
 body="""
  <h2>Hvad er en AI-implementering, og hvorfor går den ofte i stå?</h2>
  <p>En AI-implementering er det arbejde, der gør en AI-model til en fast del af hverdagen: valg af værktøj, regler for data, opsætning, oplæring og opfølgning. Den går i stå, når man behandler den som et indkøb og ikke som en ny måde at arbejde på.</p>
  <p>Tre ting går typisk galt. Ingen har ansvaret, så projektet løber ud i sandet. Ingen har valgt, hvilke opgaver Claude skal løse, så alle prøver lidt af hvert. Og ingen målte noget før start, så ingen kan vise effekten bagefter.</p>

  <h2>Trin 1: Hvem har ansvaret, og hvilke opgaver starter I med?</h2>
  <p>Udpeg én person, der har ansvaret for resultatet. Ikke en komité. Vælg derefter tre opgaver, der tager meget tid, gentager sig hver uge, og hvor et forkert svar bliver opdaget, før det gør skade. Gode kandidater er mødereferater, første udkast til tilbud, opsummering af kundehenvendelser og oprydning i CRM-data.</p>
  <p>Dårlige første kandidater er opgaver, hvor en fejl går direkte til en kunde uden kontrol, eller hvor ingen kan sige, hvad et godt resultat er.</p>

  <h2>Trin 2: Hvilken Claude-plan, og hvordan holder I data sikre?</h2>
  <p>Vælg en virksomhedsplan, ikke personlige konti. Claude Team giver fælles administration, single sign-on (SSO) og en databehandleraftale. Enterprise kommer på tale, når I har brug for automatisk oprettelse og lukning af brugere (SCIM), auditlogs eller særlige kontraktvilkår.</p>
  <p>Skriv en kort datapolitik på én side, før nogen går i gang. Den skal svare på tre spørgsmål:</p>
  <ul>
    <li>Hvilke data må gerne deles med Claude, for eksempel interne noter og offentligt materiale?</li>
    <li>Hvilke data må aldrig deles, for eksempel CPR-numre, helbredsdata og kundedata uden behandlingsgrundlag?</li>
    <li>Hvem spørger man, når man er i tvivl?</li>
  </ul>
  <p>Det er den slags dokument, en auditor spørger efter ved en ISO 27001-audit, og som Datatilsynet kan bede om. Det hjælper også med kravet om AI-færdigheder i EU's AI-forordning, som har gældt siden februar 2025. Og på én side bliver det faktisk læst.</p>

  <h2>Trin 3: Hvordan sætter I Claude op til de første arbejdsgange?</h2>
  <p>Byg hver arbejdsgang som et lille værktøj med sit eget navn. I Claude betyder det et projekt med faste instruktioner, de dokumenter, opgaven kræver, og et eksempel på et godt resultat. Et projekt til mødereferater ved, hvordan jeres referater ser ud. Et projekt til tilbud kender jeres priser og vilkår.</p>
  <figure>
    <img src="img/steps.jpg" width="1200" height="675" loading="lazy" alt="Diagram over en arbejdsgang i Claude: instruktioner, dokumenter og et godt eksempel går ind, et udkast kommer ud, og et menneske kontrollerer det">
    <figcaption>En arbejdsgang har tre input og altid et menneske i sidste led.</figcaption>
  </figure>
  <p>Når en arbejdsgang skal hente data fra CRM, mail eller kalender, kobles Claude på via connectors (integrationer). På Team og Enterprise er det en ejer af organisationen, der slår dem til, og ejeren kan begrænse en connector til kun at læse. Start med læseadgang. Giv først skriveadgang, når arbejdsgangen har kørt fejlfrit i nogle uger.</p>

  <h2>Trin 4: Hvordan lærer medarbejderne at bruge Claude i hverdagen?</h2>
  <p>Oplæring virker, når den foregår på medarbejdernes egne opgaver. En workshop med generiske eksempler er glemt inden fredag. En workshop, hvor hver deltager går derfra med sin egen færdige arbejdsgang, er i brug allerede mandag.</p>
  <p>Tre vaner gør den største forskel: Giv Claude konteksten i stedet for at regne med, at den gætter. Bed om et udkast og ikke et facit. Og læs altid resultatet igennem, før det sendes videre.</p>

  <h2>Trin 5: Hvornår giver det mening med en AI-agent på hjemmesiden?</h2>
  <p>En agent på hjemmesiden er næste skridt, når de interne arbejdsgange kører. Den svarer besøgende, stiller de spørgsmål, en sælger ville stille, og booker de rigtige møder direkte i kalenderen. Den skal være ærlig om, hvem den ikke kan hjælpe, og sende dem videre i stedet for at presse dem til et møde.</p>
  <p>Byg den ikke, før I ved, hvad en god kunde er. En agent forstærker den måde, I vurderer kundeemner på. Er den uklar, bliver agenten også uklar.</p>

  <h2>Trin 6: Hvordan måler I, om implementeringen virker?</h2>
  <p>Mål tre tal før start og igen i uge 6: hvor lang tid hver af de tre opgaver tager, hvor mange fejl kontrollen fanger, og hvor mange i teamet der bruger arbejdsgangen hver uge. Falder brugen efter tre uger, er arbejdsgangen sandsynligvis for besværlig. Ret den, før I bygger den næste.</p>
  <figure>
    <img src="img/checklist.jpg" width="1200" height="675" loading="lazy" alt="Tjekliste til AI-implementering: ejer udpeget, tre opgaver valgt, datapolitik skrevet, arbejdsgange bygget, team oplært, tal målt før og efter">
    <figcaption>Seks punkter. Mangler der et flueben, er implementeringen ikke færdig.</figcaption>
  </figure>

  <h2>Skal I gøre det selv eller have hjælp?</h2>
  <p>Mange kan nå langt selv med denne playbook. Har I ikke tid til at stå for projektet internt, eller vil I have arbejdsgangene bygget og testet på jeres egne data? Så kan I få <a href="https://brinvik.com/da" style="color:#6B1724;text-decoration:underline">AI-implementering med Claude</a> fra Brinvik. Omfanget er fast, og priserne er offentlige.</p>
""",
 faq_h="Ofte stillede spørgsmål",
 faq=[
  ("Hvor lang tid tager en AI-implementering med Claude?",
   "Opsætning og oplæring tager få dage. Det, der tager tid, er at vælge de rigtige opgaver og teste dem på rigtige data. Mål effekten i uge 6, så I har tal at tage stilling til."),
  ("Må I bruge Claude under GDPR?",
   "Ja, når opsætningen er i orden, men ansvaret ligger hos jer som dataansvarlig. Brug en virksomhedsplan, hvor Anthropics databehandleraftale indgår i de kommercielle vilkår. På virksomhedsplaner bruger Anthropic som standard ikke jeres data til at træne sine modeller. Feedback, som en bruger giver med tommel op eller ned, kan dog blive brugt, og en ejer kan slå den mulighed fra. Beslut skriftligt, hvilke data der må deles, og fjern persondata, som opgaven ikke kræver."),
  ("Hvilken Claude-plan skal I vælge?",
   "Til et team er Claude Team det naturlige udgangspunkt. Planen har fælles administration, single sign-on (SSO) og en databehandleraftale. Enterprise giver mening, når I skal bruge automatisk oprettelse og lukning af brugere (SCIM), auditlogs eller særlige kontraktvilkår. Gratis- og personlige planer hører ikke hjemme i virksomhedsdrift."),
  ("Hvordan måler I, om AI-implementeringen virker?",
   "Mål, hvor lang tid opgaven tager før og efter, hvor mange fejl kontrollen fanger, og hvor mange i teamet der bruger arbejdsgangen hver uge. Mål tallene, før I starter, ellers er der intet at sammenligne med."),
 ],
 src_h="Kilder",
 foot1="Claude-playbook. Udgivet af Brinvik, København. Tekst og billeder må deles med kildeangivelse (CC BY 4.0).",
 foot2='Denne side sætter ingen cookies og indsamler selv ingen data. Den hostes af GitHub Pages, som kan logge IP-adresser af sikkerhedshensyn. <a href="privatliv.html">Privatlivspolitik</a>',
 home="https://brinvik.com/da",
)
L["en"] = dict(
 lang="en", locale="en_GB", path="en/", css="../style.css", img="../img/", sfx="-en",
 title="Claude implementation for companies: an open playbook",
 desc="How a company of 5 to 80 people gets Claude into everyday work: choosing a plan, data and GDPR, the first workflows, training and measurement. A free six-step playbook.",
 og_title="Claude implementation for companies: an open playbook",
 og_desc="Six steps from first login to measurable results. Written for companies of 5 to 80 people.",
 brand="Claude playbook", nav='<a href="../" hreflang="da">Dansk</a> <a href="./" aria-current="page">English</a>',
 hero_alt="Six steps of a Claude implementation, from naming an owner to measuring results, shown as a timeline",
 lead="Most companies start with Claude the same way. Someone opens an account, a few colleagues try it, and three months later nobody knows whether it's made a difference. This playbook is the six steps that turn a trial into everyday use. It's written for companies of 5 to 80 people and is free to use and share.",
 byline="Published by Brinvik, October 2026. Facts checked against Anthropic's own documentation in October 2026. Sources are listed at the end.",
 body="""
  <h2>What is an AI implementation, and why does it stall?</h2>
  <p>An AI implementation is the work that makes a model a regular part of the working week: choosing the tool, setting data rules, setup, training and follow-up. It stalls when it's treated as a purchase rather than a change in how people work.</p>
  <p>Three things usually go wrong. Nobody owns it, so it drifts. Nobody chose which tasks Claude should handle, so everyone tries a bit of everything. And nobody measured anything first, so nobody can show the effect afterwards.</p>

  <h2>Step 1: Who owns it, and which tasks come first?</h2>
  <p>Name one person who owns the result. Not a committee. Then pick three tasks that take a lot of time, repeat every week, and where a wrong answer is caught before it does harm. Good candidates are meeting notes, first drafts of proposals, summaries of customer enquiries and CRM clean-up.</p>
  <p>Poor first candidates are tasks where a mistake goes straight to a customer with no check, or where nobody can say what a good result looks like.</p>

  <h2>Step 2: Which Claude plan, and how do you keep data safe?</h2>
  <p>Choose a business plan, not personal accounts. Claude Team gives you shared admin, single sign-on (SSO) and a data processing agreement. Enterprise comes in when you need automated user provisioning (SCIM), audit logs or specific contract terms.</p>
  <p>Write a one-page data policy before anyone starts. It answers three questions:</p>
  <ul>
    <li>Which data may be shared with Claude, for example internal notes and public material?</li>
    <li>Which data must never be shared, for example national ID numbers, health data and customer data without a lawful basis?</li>
    <li>Who do people ask when they're unsure?</li>
  </ul>
  <p>It's the kind of document an auditor asks for in an ISO 27001 audit, and that a data protection authority can ask to see. It also supports the AI literacy requirement in the EU AI Act, which has applied since February 2025. And at one page, people actually read it.</p>

  <h2>Step 3: How do you set Claude up for the first workflows?</h2>
  <p>Build each workflow as a small tool with its own name. In Claude that means a project with fixed instructions, the documents the task needs, and one example of a good result. A meeting notes project knows what your notes look like. A proposal project knows your prices and terms.</p>
  <figure>
    <img src="../img/steps-en.jpg" width="1200" height="675" loading="lazy" alt="Diagram of a Claude workflow: instructions, documents and a good example go in, a draft comes out, and a person reviews it">
    <figcaption>A workflow has three inputs and always a person at the end.</figcaption>
  </figure>
  <p>When a workflow needs data from the CRM, email or calendar, Claude uses connectors. On Team and Enterprise, an owner of the organisation turns them on, and can limit a connector to reading only. Start with read access. Allow writing only after the workflow has run cleanly for a few weeks.</p>

  <h2>Step 4: How do employees learn to use Claude every day?</h2>
  <p>Training works when it happens on people's own tasks. A workshop with generic examples is forgotten by Friday. A workshop where each person leaves with their own finished workflow is in use on Monday.</p>
  <p>Three habits matter most: give Claude the context instead of hoping it guesses, ask for a draft rather than a final answer, and always read the result before passing it on.</p>

  <h2>Step 5: When does a Claude agent on your website make sense?</h2>
  <p>A website agent is the next step once the internal workflows are running. It answers visitors, asks the questions a salesperson would ask, and books the right meetings straight into the calendar. It should be honest about who it can't help, and refer them on rather than push them into a meeting.</p>
  <p>Don't build it until you know what a good customer looks like. An agent amplifies how you qualify leads. If your criteria are vague, so is the agent.</p>

  <h2>Step 6: How do you measure whether it works?</h2>
  <p>Measure three numbers before you start and again in week 6: how long each of the three tasks takes, how many errors review catches, and how many people use the workflow each week. If use drops after three weeks, the workflow is probably too awkward. Fix it before you build the next one.</p>
  <figure>
    <img src="../img/checklist-en.jpg" width="1200" height="675" loading="lazy" alt="Claude implementation checklist: owner named, three tasks chosen, data policy written, workflows built, team trained, numbers measured before and after">
    <figcaption>Six items. If one isn't ticked, the implementation isn't done.</figcaption>
  </figure>

  <h2>Do it yourself, or get help?</h2>
  <p>Many teams get a long way on their own with this playbook. Don't have the time to own it internally, or want the workflows built and tested on your own data? Brinvik offers a <a href="https://brinvik.com/en/services/internal-ai-tools" style="color:#6B1724;text-decoration:underline">Claude implementation for teams</a>, with a fixed scope and public prices.</p>
""",
 faq_h="Frequently asked questions",
 faq=[
  ("How long does a Claude implementation take?",
   "Setup and training take a few days. What takes time is picking the right tasks and testing them on real data. Measure the effect in week 6, so you have numbers to base a decision on."),
  ("Can you use Claude under GDPR?",
   "Yes, if it's set up properly, but the responsibility stays with you as data controller. Use a business plan, where Anthropic's data processing agreement is part of the commercial terms. On business plans, Anthropic doesn't use your data to train its models by default. Feedback a user gives with thumbs up or down can be used, though, and an owner can switch that option off. Decide in writing which data may be shared, and remove personal data the task doesn't need."),
  ("Which Claude plan should a company choose?",
   "For a team, Claude Team is the natural start. It has shared admin, single sign-on (SSO) and a data processing agreement. Enterprise makes sense when you need automated user provisioning (SCIM), audit logs or specific contract terms. Free and personal plans don't belong in company operations."),
  ("How do you measure whether it works?",
   "Measure how long the task takes before and after, how many errors review catches, and how many people on the team use the workflow each week. Take the numbers before you start, or there's nothing to compare with."),
 ],
 src_h="Sources",
 foot1="Claude playbook. Published by Brinvik, Copenhagen. Text and images may be shared with attribution (CC BY 4.0).",
 foot2='This page sets no cookies and collects no data itself. It is hosted on GitHub Pages, which may log IP addresses for security. <a href="../privacy.html">Privacy</a>',
 home="https://brinvik.com/en",
)

def page(k):
    S = L[k]; url = f"{BASE}/{S['path']}"
    hero = f"{BASE}/img/hero{S['sfx']}.jpg"
    ld = {"@context": "https://schema.org", "@graph": [
      {"@type": "Article", "headline": S["title"], "inLanguage": S["lang"], "datePublished": DATE, "dateModified": DATE,
       "image": hero, "mainEntityOfPage": url,
       "author": {"@type": "Organization", "name": "Brinvik", "url": S["home"]},
       "publisher": {"@type": "Organization", "name": "Brinvik", "url": S["home"]}},
      {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in S["faq"]]}]}
    faq = "\n".join(f"  <h3>{html.escape(q)}</h3>\n  <p>{html.escape(a)}</p>" for q, a in S["faq"])
    src = "\n".join(f'    <li><a href="{u}">{html.escape(t[k])}</a></li>' for u, t in SRC)
    return f"""<!doctype html>
<html lang="{S['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{S['title']}</title>
<meta name="description" content="{S['desc']}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="da" href="{BASE}/">
<link rel="alternate" hreflang="en" href="{BASE}/en/">
<link rel="alternate" hreflang="x-default" href="{BASE}/en/">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{S['og_title']}">
<meta property="og:description" content="{S['og_desc']}">
<meta property="og:image" content="{hero}">
<meta property="og:image:width" content="1600">
<meta property="og:image:height" content="900">
<meta property="og:locale" content="{S['locale']}">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="{S['css']}">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=1)}
</script>
</head>
<body>
<header class="top">
  <a class="brand" href="./">{S['brand']}</a>
  <nav>{S['nav']}</nav>
</header>

<main class="article">
  <figure class="hero">
    <img src="{S['img']}hero{S['sfx']}.jpg" width="1600" height="900" alt="{S['hero_alt']}">
  </figure>

  <h1>{S['title']}</h1>
  <p class="lead">{S['lead']}</p>

  <p class="byline">{S['byline']}</p>
{S['body']}
  <h2>{S['faq_h']}</h2>
{faq}

  <h2>{S['src_h']}</h2>
  <ul class="sources">
{src}
  </ul>
</main>

<footer class="foot">
  <p>{S['foot1']}</p>
  <p>{S['foot2']}</p>
</footer>
</body>
</html>
"""

os.makedirs(f"{OUT}/en", exist_ok=True)
open(f"{OUT}/index.html", "w", encoding="utf-8").write(page("da"))
open(f"{OUT}/en/index.html", "w", encoding="utf-8").write(page("en"))

PRIV = {
 "da": ("privatliv.html", "da", "Privatlivspolitik | Claude-playbook", "Claude-playbook", "./",
   '<a href="./">Dansk</a> <a href="privacy.html" hreflang="en">English</a>',
   "Privatlivspolitik",
   "Siden udgives af Brinvik, København.",
   [("Hvad indsamler siden?", "Siden indsamler ikke selv noget. Den har ingen formularer, ingen cookies, ingen analyse og ingen sporing. Værten kan dog logge IP-adresser (se nedenfor)."),
    ("Hvem hoster siden?", "Siden hostes af GitHub Pages (GitHub, Inc., USA). GitHub kan registrere besøgendes IP-adresse af sikkerhedshensyn. Data kan derfor blive behandlet uden for EU under GitHubs egne vilkår og databeskyttelsesrammen mellem EU og USA."),
    ("Kontakt", "Har du spørgsmål om privatliv, kan du skrive via kontaktsiden på brinvik.com.")],
   "Senest opdateret: 20. oktober 2026."),
 "en": ("privacy.html", "en", "Privacy | Claude playbook", "Claude playbook", "en/",
   '<a href="privatliv.html" hreflang="da">Dansk</a> <a href="en/">English</a>',
   "Privacy",
   "This site is published by Brinvik, Copenhagen.",
   [("What does this site collect?", "Nothing itself. It has no forms, no cookies, no analytics and no tracking. The host may log IP addresses (see below)."),
    ("Who hosts it?", "The site is hosted on GitHub Pages (GitHub, Inc., USA). GitHub may log visitor IP addresses for security. Data may therefore be processed outside the EU under GitHub's own terms and the EU-US Data Privacy Framework."),
    ("Contact", "Privacy questions go through the contact page on brinvik.com.")],
   "Last updated: 20 October 2026."),
}
for k, (fn, lang, t, brand, home, nav, h1, p1, secs, upd) in PRIV.items():
    body = "\n".join(f"<h2>{h}</h2><p>{p}</p>" for h, p in secs)
    open(f"{OUT}/{fn}", "w", encoding="utf-8").write(f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{t}</title><meta name="robots" content="noindex"><link rel="stylesheet" href="style.css"></head><body>
<header class="top"><a class="brand" href="{home}">{brand}</a><nav>{nav}</nav></header>
<main class="article"><h1>{h1}</h1>
<p>{p1}</p>
{body}
<p>{upd}</p></main></body></html>
""")
print("ok")
