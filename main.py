from fastapi import FastAPI
from routers.rate_limiter import router_current
from utils.exceptions import global_exception_handler, validation_exception_handler
from fastapi.exceptions import RequestValidationError

app = FastAPI()

#Initializes your FastAPI() application
#Registers routes and logic
#Mounts exception handlers



# Register routes
app.include_router(router_current, prefix="/api/v1")

# Register global exception handlers
app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)