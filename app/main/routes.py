from flask import jsonify, request
         
from app.main import bp  # noqa
from app.database import DB
from app.models.job import Job 
from bson.json_util import dumps


@bp.route('/', methods = ['GET'])
def jobs():
    """Get all jobs"""
    result = DB.find("jobs")
    print(result)
    if result:
        return dumps(result)
    else:
        return ({"response": "no user found for"})
        
        
@bp.route('/add_job', methods = ['POST'])
def add_job():
    """Add json to the database."""
    content = request.get_json()
    print(content)
    DB.insert(collection='jobs', data=content)
    return ('', 204)

@bp.route('/add_default_job', methods = ['POST'])
def add_default_job():
    """Adds job5 to the database."""
    new_job = Job(name='job50')
    new_job.insert() 
    return ('', 204)
