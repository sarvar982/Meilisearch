import routes.route
from core.config import conf
from fastapi import FastAPI
from routes.csvjob import index_from_csv





app = FastAPI()
conf()
app.include_router(routes.route.router)

# csv_filename = 'prisma_public_community.csv'
# index_from_csv(csv_filename)

