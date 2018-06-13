SELECT concat(clients.first_name," ",clients.last_name) as client_full_name, count(*) as total_leads FROM clients
JOIN sites on clients.client_id = sites.client_id
JOIN leads on sites.site_id = leads.site_id
GROUP BY clients.client_id