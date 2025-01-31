from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from gae_bingo import cache
from gae_bingo import dashboard
from gae_bingo import middleware
from gae_bingo import plots
from gae_bingo import blotter

application = webapp.WSGIApplication([
    ("/gae_bingo/persist", cache.PersistToDatastore),
    ("/gae_bingo/log_snapshot", cache.LogSnapshotToDatastore),
    ("/gae_bingo/dashboard", dashboard.Dashboard),
    ("/gae_bingo/dashboard/control_experiment", dashboard.ControlExperiment),
    ("/gae_bingo/dashboard/plot_experiment", plots.Timeline),
    ("/gae_bingo/blotter/ab_test", blotter.AB_Test),
    ("/gae_bingo/blotter/bingo", blotter.Bingo),
])
application = middleware.GAEBingoWSGIMiddleware(application)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

