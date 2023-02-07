# Be sure to export your API key first
import meraki
dashboard = meraki.DashboardAPI(API_KEY)
my_orgs = dashboard.organizations.getOrganizations()
