"""Starter content, loaded into the database the first time the app runs.
Review every line and adjust it to what RAMS Digital Solutions really offers."""

SERVICES = [
 dict(slug="graphic-design", title="Graphic Design", icon="design",
  tagline="Logos and visuals that make your business look as good as it works.",
  intro="Your brand is often the first thing a customer sees. We design clean, consistent visuals that look sharp on screen and in print.",
  groups=[
   dict(title="Brand Identity", blurb="A look that people recognise and remember.", items=[
     dict(name="Logo Design", desc="Original logos delivered in the formats you need."),
     dict(name="Colour & Typography", desc="A simple palette and font set used consistently."),
     dict(name="Brand Starter Packs", desc="Logo variations ready for social media, documents and signage.")]),
   dict(title="Marketing Material", blurb="Designs that get read.", items=[
     dict(name="Business Cards", desc="Print-ready cards that match your brand."),
     dict(name="Flyers & Posters", desc="Promotions, events and product launches."),
     dict(name="Social Media Graphics", desc="Post and banner designs sized for each platform.")])],
  faqs=[
   dict(q="Can you design a logo from scratch?", a="Yes. Tell us about your business and the look you want, and we'll create original concepts and refine the one you choose."),
   dict(q="Can you also print what you design?", a="Yes. Our printing and branding service covers business cards, flyers and branded items, so design and print stay under one roof."),
   dict(q="How do I get started?", a="Send us a WhatsApp message describing what you need. We'll reply with next steps and a quote.")],
  related=["printing-branding", "website-development"]),

 dict(slug="printing-branding", title="Printing & Branding", icon="print",
  tagline="From business cards to branded items, printed properly.",
  intro="Good design deserves good print. We take your artwork from screen to finished product, so your brand looks the same everywhere customers meet it.",
  groups=[
   dict(title="Business Printing", blurb="The everyday print every business needs.", items=[
     dict(name="Business Cards", desc="Clean, durable cards in the finish you prefer."),
     dict(name="Flyers & Brochures", desc="Promotional print for handouts and counters."),
     dict(name="Posters & Banners", desc="Large-format print for shops, events and promotions.")]),
   dict(title="Branded Items", blurb="Put your logo where people will see it.", items=[
     dict(name="Branded Clothing", desc="Uniforms and team wear with your logo."),
     dict(name="Stationery", desc="Letterheads, invoices and envelopes that match your brand."),
     dict(name="Signage", desc="Shopfront and office signage that gets you noticed.")])],
  faqs=[
   dict(q="Do I need to supply my own design?", a="No. If you have artwork we'll print it; if you don't, our graphic design service can create it first."),
   dict(q="Can you print small quantities?", a="Often, yes. Message us with what you need and the quantity and we'll confirm what's possible."),
   dict(q="How long does printing take?", a="It depends on the item and quantity. Ask us on WhatsApp for a realistic turnaround for your job.")],
  related=["graphic-design", "website-development"]),

 dict(slug="website-development", title="Website Development", icon="web",
  tagline="Fast, mobile-friendly websites that turn visitors into customers.",
  intro="We build professional websites that load quickly, work on every screen and make it easy for customers to contact you.",
  groups=[
   dict(title="Websites", blurb="The right site for how you do business.", items=[
     dict(name="Business Websites", desc="Clear service pages with a prominent way to contact you."),
     dict(name="Portfolio Websites", desc="Showcase your work, your team or your story."),
     dict(name="E-commerce Stores", desc="Product catalogues, online payments and order management.")]),
   dict(title="Built to Perform", blurb="Details that help you get found and trusted.", items=[
     dict(name="Mobile-First Design", desc="Layouts that work properly on phones first."),
     dict(name="Search-Friendly Structure", desc="Clean markup and page structure that search engines understand."),
     dict(name="Updates & Support", desc="Help keeping your site current after launch.")])],
  faqs=[
   dict(q="Is a website the same as custom software?", a="No. A website is how customers find you; software is how your business runs. We can build either, and they are different jobs."),
   dict(q="Can I update the website myself?", a="We can set your site up so common changes are simple, and we're available for anything more involved."),
   dict(q="Do you handle domains and hosting?", a="Yes, we can help you choose and set these up so everything is ready at launch.")],
  related=["graphic-design", "it-support"]),

 dict(slug="it-support", title="IT Support", icon="support",
  tagline="Practical help when your computers, software or email let you down.",
  intro="Technology should stay out of your way. We keep your devices and systems running, and fix problems quickly when they appear.",
  groups=[
   dict(title="Everyday Support", blurb="Fast help for the issues that slow your team down.", items=[
     dict(name="Troubleshooting & Repairs", desc="Diagnosis and fixes for computers and devices."),
     dict(name="Software Installation", desc="Setup and configuration of the programs you rely on."),
     dict(name="Printer & Device Setup", desc="Printers, scanners and peripherals working properly.")]),
   dict(title="Business Essentials", blurb="Protect your data and keep everyone connected.", items=[
     dict(name="Email Setup", desc="Professional email on your own business domain."),
     dict(name="Data Backup", desc="Simple backup routines so one failure doesn't cost you everything."),
     dict(name="Security Basics", desc="Updates, antivirus and good-practice advice for your team.")])],
  faqs=[
   dict(q="Do you offer on-site and remote support?", a="Ask us on WhatsApp for what's available in your area; many issues can be solved remotely."),
   dict(q="Can you support a small office?", a="Yes. Small offices are exactly who we help: a few computers, a network, a printer and email that needs to just work."),
   dict(q="What if I'm not sure what the problem is?", a="Describe what's happening and we'll tell you the likely cause and the quickest fix.")],
  related=["networking", "cctv-solutions"]),

 dict(slug="networking", title="Networking Solutions", icon="network",
  tagline="Reliable wired and wireless networks for homes, shops and offices.",
  intro="A good network is invisible: it simply works. We design and install networks that keep your people, devices and systems connected.",
  groups=[
   dict(title="Network Setup", blurb="Built properly from the start.", items=[
     dict(name="Office & Shop Networks", desc="Wired and wireless networks sized for your premises."),
     dict(name="Structured Cabling", desc="Neat, labelled cabling that's easy to maintain."),
     dict(name="Routers & Switches", desc="Configuration of the equipment that runs your network.")]),
   dict(title="Wi-Fi & Reliability", blurb="Connections you can depend on.", items=[
     dict(name="Wi-Fi Coverage", desc="Fixing dead spots and slow connections."),
     dict(name="Network Troubleshooting", desc="Finding and fixing drops, slowdowns and faults."),
     dict(name="Upgrades & Expansion", desc="Growing your network as your business grows.")])],
  faqs=[
   dict(q="Can you fix weak Wi-Fi in my building?", a="Usually, yes. The fix depends on the layout and equipment, so send us details and we'll recommend the best approach."),
   dict(q="Do you install network cabling?", a="Yes. We can plan and install cabling for new setups or tidy up an existing one."),
   dict(q="Can you network my CCTV cameras too?", a="Yes. Our CCTV service includes the cabling and network setup for remote viewing.")],
  related=["cctv-solutions", "it-support"]),

 dict(slug="cctv-solutions", title="CCTV Solutions", icon="cctv",
  tagline="Security camera systems you can check from your phone.",
  intro="Keep an eye on what matters. We plan, install and set up CCTV systems for homes and businesses, with remote viewing so you can check in anywhere.",
  groups=[
   dict(title="Installation", blurb="Cameras placed where they count.", items=[
     dict(name="Site Assessment", desc="We look at your premises and recommend camera positions."),
     dict(name="Camera Installation", desc="Professional mounting and neat cabling."),
     dict(name="Recorder Setup", desc="DVR/NVR configuration and storage set up properly.")]),
   dict(title="Viewing & Care", blurb="Stay in the loop and keep it working.", items=[
     dict(name="Remote Viewing", desc="Watch live footage on your phone or computer."),
     dict(name="Maintenance & Repairs", desc="Servicing, fault finding and replacements."),
     dict(name="System Upgrades", desc="Add cameras or improve an existing system.")])],
  faqs=[
   dict(q="Can I watch my cameras on my phone?", a="Yes. We set up remote viewing so you can check live footage from wherever you are."),
   dict(q="Can you add cameras to my existing system?", a="Often, yes. Tell us what you have and we'll advise on the best way to expand it."),
   dict(q="Do you do homes as well as businesses?", a="Yes, both. Message us a few details about the property and what you want to cover.")],
  related=["networking", "it-support"]),
]
