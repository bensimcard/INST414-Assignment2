import requests
from bs4 import BeautifulSoup
import networkx as nx
import matplotlib.pyplot as plt

# The subset of nodes we are analyzing
tech_companies = [
    'Apple_Inc.', 'Microsoft', 'Google', 'Amazon_(company)', 
    'Meta_Platforms', 'IBM', 'Intel', 'Cisco', 
    'Oracle_Corporation', 'Nvidia', 'Salesforce', 
    'Adobe_Inc.', 'Netflix', 'Uber', 'Tesla,_Inc.'
]

base_url = "https://en.wikipedia.org/wiki/"
edges = set() 

# This fake ID tells Wikipedia we are a normal web browser, not a bot.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print("Scraping Wikipedia pages (Paragraphs ONLY to avoid navboxes)...")

for company in tech_companies:
    print(f"  Scraping {company.replace('_', ' ')}...")
    url = base_url + company
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    content = soup.find(id="mw-content-text")
    if not content:
        print(f"    [!] Warning: Could not find content for {company}")
        continue
        
    # THE FIX: Only look inside paragraph tags to avoid massive Wikipedia footer tables
    paragraphs = content.find_all('p')
    links_found_for_this_company = 0
    
    for p in paragraphs:
        links = p.find_all('a')
        for link in links:
            href = link.get('href', '')
            if href.startswith('/wiki/'):
                target = href.split('/wiki/')[1]
                if target in tech_companies and target != company:
                    edges.add((company, target))
                    links_found_for_this_company += 1
                
    print(f"    -> Found {links_found_for_this_company} organic links to other tech giants.")

print(f"\nTotal edges (connections) found: {len(edges)}")

# graph
G = nx.DiGraph() 
G.add_nodes_from(tech_companies)
G.add_edges_from(edges)

# importance
in_degrees = dict(G.in_degree())
sorted_companies = sorted(in_degrees.items(), key=lambda x: x[1], reverse=True)

print("\n--- TOP 3 MOST IMPORTANT TECH COMPANIES (By Organic In-Degree Centrality) ---")
for i in range(3):
    name = sorted_companies[i][0].replace('_', ' ')
    score = sorted_companies[i][1]
    print(f"{i+1}. {name} (Linked to by {score} other tech giants)")

# visualizing the network
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(G, k=0.8, seed=42) 

nx.draw(G, pos, with_labels=True, node_color='lightgreen', 
        node_size=3000, font_size=9, font_weight='bold', 
        edge_color='gray', arrows=True, arrowsize=20, alpha=0.7)

plt.title("The Silicon Valley Web: Organic Network", fontsize=16)
plt.savefig("tech_network_organic.png", format="PNG", bbox_inches="tight")
print("\nGraph saved as 'tech_network_organic.png'!")