<div align="center">
 
# Sanket Sharma 
 
**Software Engineer · Systems Thinker · AI & Markets**

[![Email](https://img.shields.io/badge/Email-sanket%40signaloninternet.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:sanket@signaloninternet.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-signalinternet-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/signalinternet/)
[![Website](https://img.shields.io/badge/Website-signaloninternet.com-6366F1?style=flat-square&logo=safari&logoColor=white)](https://www.signaloninternet.com/)
</div>

## Hey, I'm Sanket

I'm 21, currently in my pre-final year studying CS with a focus on AI and ML. But honestly I've been building things since long before college started, websites, apps, backends, payment systems, whatever the problem needed. 

Over the last 4 years I've shipped real software for real clients. Not side projects that live on localhost. Actual production systems with real users, real payments, and real consequences when something breaks. I've worked with US-based startups as a contract engineer while still being a full-time student, and I've built some fairly complex platforms entirely on my own from architecture to deployment.            

Right now I'm most drawn to problems at the intersection of AI and financial systems, the kind of work where strong engineering meets genuine mathematical depth. I have a strong math foundation and I'm actively pushing deeper into that space.

If you want to see what I actually build, keep reading. 

---

## 📊 GitHub Activity

<div align="center">

🔥 **Daily**

<img src="https://streak-stats.demolab.com?user=signaloninternet&theme=rose-pine&hide_border=true&date_format=j%20M%5B%20Y%5D&mode=daily&fire=F97316&ring=8B5CF6&currStreakLabel=8B5CF6&sideLabels=6B7280&dates=6B7280&stroke=1F1F2E&background=0F0F1A&currStreakNum=F97316&sideNums=E2E8F" alt="Daily Streak" />

📅 **Weekly**

<img src="https://streak-stats.demolab.com?user=signaloninternet&theme=rose-pine&hide_border=true&date_format=j%20M%5B%20Y%5D&mode=weekly&fire=8B5CF6&ring=F97316&currStreakLabel=F97316&sideLabels=6B7280&dates=6B7280&stroke=1F1F2E&background=0F0F1A&currStreakNum=8B5CF6&sideNums=E2E8F0" alt="Weekly Streak" />

</div>

---

## 🛠️ What I work with

I mostly live in TypeScript and Python. On the frontend it's React, Next.js, and React Native depending on what we're building. Backend is Node.js or FastAPI, Supabase for most projects (PostgreSQL under the hood with RLS doing the heavy lifting), Redis when I need caching or queues, and AWS for infrastructure. I've wired up Stripe Connect, Twilio, SendGrid, and a handful of Indian payment gateways into production systems. On the AI side I've worked with PyTorch, Scikit-Learn, XGBoost, Gemini API, and I'm pushing deeper into that stack.

<div align="center">

![TypeScript](https://img.shields.io/badge/TypeScript-0F0F1A?style=for-the-badge&logo=typescript&logoColor=3178C6)
![JavaScript](https://img.shields.io/badge/JavaScript-0F0F1A?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![Python](https://img.shields.io/badge/Python-0F0F1A?style=for-the-badge&logo=python&logoColor=3776AB)
![C++](https://img.shields.io/badge/C++-0F0F1A?style=for-the-badge&logo=cplusplus&logoColor=00599C)
![SQL](https://img.shields.io/badge/SQL-0F0F1A?style=for-the-badge&logo=postgresql&logoColor=4169E1)

![React](https://img.shields.io/badge/React-0F0F1A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Next.js](https://img.shields.io/badge/Next.js-0F0F1A?style=for-the-badge&logo=next.js&logoColor=white)
![React Native](https://img.shields.io/badge/React_Native-0F0F1A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Remix](https://img.shields.io/badge/Remix-0F0F1A?style=for-the-badge&logo=remix&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind-0F0F1A?style=for-the-badge&logo=tailwindcss&logoColor=06B6D4)

![Node.js](https://img.shields.io/badge/Node.js-0F0F1A?style=for-the-badge&logo=node.js&logoColor=339933)
![Supabase](https://img.shields.io/badge/Supabase-0F0F1A?style=for-the-badge&logo=supabase&logoColor=3ECF8E)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-0F0F1A?style=for-the-badge&logo=postgresql&logoColor=4169E1)
![Redis](https://img.shields.io/badge/Redis-0F0F1A?style=for-the-badge&logo=redis&logoColor=DC382D)
![AWS](https://img.shields.io/badge/AWS-0F0F1A?style=for-the-badge&logo=amazonaws&logoColor=FF9900)
![Docker](https://img.shields.io/badge/Docker-0F0F1A?style=for-the-badge&logo=docker&logoColor=2496ED)

![PyTorch](https://img.shields.io/badge/PyTorch-0F0F1A?style=for-the-badge&logo=pytorch&logoColor=EE4C2C)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-0F0F1A?style=for-the-badge&logo=scikitlearn&logoColor=F7931E)
![Gemini](https://img.shields.io/badge/Gemini_API-0F0F1A?style=for-the-badge&logo=google&logoColor=4285F4)

</div>

---

## 💼 Where I've worked

### OceanWaveWeb LLC | Software Engineer
**Mar 2025 to Present · Remote, US**

This was the most intense stretch of building I've done. I was the only engineer. No senior to ask questions, no one to review architecture decisions, no team to split the work. Just me and two very large, very real platforms that needed to be designed and shipped.

**The first was OceanWave Brain**, a full agency operating system. The idea was to replace all the scattered tools an agency uses (project management, client communication, billing, time tracking, sales pipeline) with one unified platform that has proper role separation. I built it with React, Vite, and Supabase on the backend.

The four roles (admin, super_admin, employee, and client) each have completely isolated access. This isn't handled in the frontend with if-statements. The RLS policies in Postgres enforce it at the database level, so even if someone bypassed the UI, they'd hit a wall. The agency side has a full CRM, workspace and task management, time tracking, team roster, and a sales pipeline. I also plugged in Gemini API to give AI-powered summaries and insights on tasks and finances, and Stream for real-time video huddles inside the platform.

The billing side was the most complex part. I implemented Stripe Connect from scratch: seller onboarding, public checkout pages by order ID, webhook-based payment sync, and automated fee transfer logic between connected accounts. Then on top of that I built a completely separate platform payments API for third-party business apps to integrate with. Their own onboarding, API key management, subscription billing, and webhook processing. Two independent payment systems, one codebase.

The last piece was a public Edge API layer. External websites (what we called "skins") could fetch a client's live profile content (products, services, gallery, blogs) purely by username. Essentially a headless CMS that external devs could build on top of.

```
Agency Dashboard  ──┐
Client Portal     ──┤──► Supabase (PostgreSQL + RLS + Edge Functions)
External Skins    ──┘         │
                              ├──► Stripe Connect
                              ├──► Platform Payments API
                              └──► Stream Video
```

**The second was a Valet Parking Operations Platform**, and this one is actually live at a restaurant right now. Real staff using it every shift.

The problem was simple on the surface: a valet operation needed to go fully digital. But once you start modeling it properly, it gets complicated fast. You have multiple staff on the same shift modifying the same ticket queue simultaneously. You have guests who need to request their car from their phone without creating an account. You have a restaurant owner who needs to see revenue numbers in real time. And you have payments that need to flow through WhatsApp, SMS, or email depending on what the guest prefers.

I built three separate surfaces. The mobile app (React Native + Expo) is what staff use on shift. They sign in, open a shift, check vehicles in, assign them to zones and key slots, manage the queue, collect payment, and close out. The admin console (Next.js) is what the restaurant owner uses: full location management, staff assignment and approval, rate configuration, shift management, and a finance dashboard. The customer portal is a simple tokenized page (`/t/{token}`) where guests can request their car and pay digitally, no login required.

The ticket moves through four states: active → requested → ready → completed. What I'm proud of is that this isn't enforced in the app code. PostgreSQL triggers handle the state transitions and auto-generate invoice rows the moment a ticket is created. RLS policies mean staff can only ever see and operate on tickets at their assigned location. It's not a filter I apply in the query. It's enforced by the database before the query even runs.

The payment flow goes through a single Supabase Edge Function that creates the payment intent, generates a short link (`/p/{code}`), fires it off via Twilio or SendGrid, logs the delivery to an audit table, and if the payment provider returns a client secret instead of a redirect, the hosted `/pay/{code}` page handles the card confirmation. Every single step is logged.

```
Staff checks in vehicle
        │
        ▼
Ticket goes active → zone, spot, key slot assigned
        │
        ▼
Guest gets link → requests car via /t/{token}
        │
        ▼
Staff retrieves car → ticket goes ready → payment collected
        │
        ▼
Ticket completed → invoice finalized → shows in v_revenue_daily
```

On top of these two platforms I also delivered 12+ production websites for clients using Next.js and TypeScript (consistently hitting 95 to 100 on PageSpeed) and built a multi-tenant restaurant ordering system in React Native that's live across 11+ branches.

---

### Mediamaxxing LLC | Software Engineer
**Nov 2025 to February 2025 · Remote, US**

I joined to help build AI tooling for content workflows. The main thing I built was a video and content editing pipeline powered by Gemini API that cut manual processing time by 60%. I also designed a content quality and spam scoring engine for TikTok, YouTube, and Instagram. It looks at engagement patterns, metadata signals, and sentiment to flag low-quality or inauthentic content. Beyond that I've been in the trenches fixing production issues (1,400+ closed) and pushing code constantly (300+ PRs merged), while also working on Redis caching and AWS optimization to keep the platform fast under load.

---

### CyberFlux Enterprises | Frontend Developer
**Nov 2024 to Mar 2025 · Remote, India**

My first proper engineering role. I built the frontend for a custom apparel design platform and worked on NeuraSim.Health, which ended up being featured on Shark Tank India. Reduced load times by 30% through proper asset optimization and component architecture.

---

### PhonePe | Business Development Executive
**Feb 2023 to Aug 2023 · Thane, India**

Before I went fully into engineering I spent 7 months in sales at PhonePe. I'm glad I did it. Understanding how business and revenue actually work made me a better engineer. Got 100% adoption on new product launches within two weeks, drove 21% revenue growth in my sector.

---

## 🚀 Things I've built outside of work

**[stash.market](https://www.stash.market/)** is a no-code commerce platform I built for people who want to sell things online without hiring a developer. You fill out some forms, connect a payment method, and you have a working store with inventory management, a WhatsApp storefront, and Indian payment gateway support. There's a real client on it right now managing over ₹20 lakhs in inventory. The backend uses Celery and Redis workers to handle orders and notifications asynchronously so nothing blocks.

**[SuprBuy](https://www.suprbuy.com/)** tracks prices across Indian e-commerce sites in real time. I built Puppeteer scraping pipelines and Node.js workers to pull data at scale, and the site loads in under 2 seconds using server-side rendering and aggressive caching.

**AI University Finder** was a fun one. I scraped over 100 university websites, built a matching engine that reads a student's resume and skills and maps them to relevant programs, and set up automated WhatsApp notifications when good matches come up. It was my first serious NLP project and it actually works well.

**Swipify** is a React Native app that helps people clean up their camera rolls using on-device ML. Tinder-style swipe interface, everything runs locally so no photos leave your phone.

---

## 🧠 Something I think about a lot

GDP is a bad measure of how a country is actually doing. It captures output but misses almost everything that matters: how knowledge compounds, how fast technology is being adopted, whether people have real opportunity. I've been building a framework that tries to model these things more honestly, pulling in variables like innovation output, human capital accumulation, and sustainability alongside the traditional indicators. It's early work but it's the kind of problem I'd like to spend real time on eventually.

It's also why I'm drawn to quant and AI roles in finance. The interesting work there is fundamentally about building better models of reality.

---

<div align="center">

*If you're working on something genuinely hard, especially at the intersection of AI and markets, I want to hear about it.*

[![Get In Touch](https://img.shields.io/badge/Get%20In%20Touch-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sanket@signaloninternet.com)

</div>
