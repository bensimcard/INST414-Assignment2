# The Silicon Valley Web: Tech Company Network Analysis

This repository contains the Python code and data visualization for a network analysis of 15 major technology companies. By web scraping Wikipedia, this script maps the organic connections between these tech giants to determine the foundational core of the modern B2B ecosystem.

This project was created for **INST414: Assignment 2**.

## Project Overview

The objective of this project is to answer a specific business question: **Which major technology company sits at the absolute center of the modern tech ecosystem, and which platform should a B2B SaaS startup prioritize for a software integration?**

To answer this, the included Python script:
1. **Scrapes Wikipedia:** Uses `urllib` and `BeautifulSoup` to download the official Wikipedia pages of 15 major tech companies.
2. **Filters for Organic Connections:** Explicitly targets `<p>` (paragraph) tags to avoid automated Wikipedia footer templates (like the NASDAQ-100 Navboxes). This ensures only genuine, contextual links are counted as edges.
3. **Builds a Directed Graph:** Uses `NetworkX` to create a network where nodes are companies and edges are directed hyperlinks from one company's article to another.
4. **Calculates Centrality:** Ranks the companies using **In-Degree Centrality** to find out which companies are most frequently referenced by the rest of the industry.
5. **Visualizes the Network:** Uses `matplotlib` to generate a node-link diagram (`tech_network_organic.png`) demonstrating the core-periphery structure of the network.

## 🛠️ Technologies & Libraries Used
* **Python 3.x**
* **BeautifulSoup4** (HTML parsing & web scraping)
* **Urllib / Regular Expressions** (HTTP requests & text extraction)
* **NetworkX** (Graph/Network creation and centrality mathematics)
* **Matplotlib** (Data visualization)
