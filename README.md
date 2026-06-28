# LifeWithPies — Portfolio Website

Personal portfolio site for a Sr. Engineer specializing in AI/ML & Quantum Computing.

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)

## Overview

A static portfolio site showcasing data engineering, analytics, and automation projects. Built on the HTML5 UP "Massively" template with custom styling (`custom.css`) layered on top. The site uses a single-page layout with a featured project hero and a responsive project grid below.

## Live Site

`https://lifewithpies.github.io`

## Projects Showcased

| Project | Stack | Link |
|---|---|---|
| Data Cleaning & Transformation in SQL | SQL Server, ETL | [GitHub](https://github.com/LifeWithPies/PortfolioProjects/blob/main/Data%20Cleaning%20Portfolio%20Project%20Queries.sql) |
| Amazon Price Scraper | Python, BeautifulSoup, Automation | [GitHub](https://github.com/LifeWithPies/PortfolioProjects/blob/main/Amazon%20Web%20Scraper%20Project.ipynb) |
| COVID-19 Forecast Dashboard | Tableau, Forecasting, Data Viz | [Tableau Public](https://public.tableau.com/app/profile/prashant7058/viz/CovidForecastDashboard_16776347612430/Dashboard1) |
| AirBnB Price Tracker | Tableau, Geospatial, Analytics | [Tableau Public](https://public.tableau.com/app/profile/prashant7058/viz/AirBnBPriceTracker/Dashboard1) |

> Additional project images (`africa.jpg`, `africa1.jpg`) are present in `/images/` and may be wired to future projects.

## Tech Stack

| Layer | Technology |
|---|---|
| Markup | HTML5 |
| Styling | CSS3, SCSS/SASS (`assets/sass/`) |
| Interactivity | JavaScript (jQuery, scrollex, scrolly, breakpoints) |
| Icons | FontAwesome (webfonts) |
| Fonts | Google Fonts — Inter, Space Grotesk |
| Base template | [HTML5 UP — Massively](https://html5up.net) |

## Site Structure

```
portfolio_website/
├── index.html          # Single-page portfolio
├── assets/
│   ├── css/
│   │   ├── main.css    # Compiled from SASS
│   │   ├── custom.css  # Project-specific overrides
│   │   └── noscript.css
│   ├── sass/           # SASS source files
│   ├── js/             # jQuery and utility scripts
│   └── webfonts/       # FontAwesome icon fonts
├── images/             # Project hero images (housing, covid, airbnb, amazon, africa, bg)
├── README.md
└── README.txt          # Original stub (kept for reference)
```

## Local Development

No build step required for viewing — open `index.html` directly in a browser:

```bash
# Option 1: open directly
open index.html

# Option 2: serve with Python for accurate relative-path behavior
python3 -m http.server 8080
# then visit http://localhost:8080
```

To edit styles, compile SASS from `assets/sass/` into `assets/css/main.css`:

```bash
sass assets/sass/main.scss assets/css/main.css --watch
```

## Contact

- LinkedIn: [LifeWithPies](https://www.linkedin.com/in/lifewithpies/)
- GitHub: [LifeWithPies](https://github.com/LifeWithPies)
