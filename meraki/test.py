# Be sure to export your API key first
# API_KEY=ehg549g5hilull4w7985go
import meraki
dashboard = meraki.DashboardAPI(API_KEY)
my_orgs = dashboard.organizations.getOrganizations()
