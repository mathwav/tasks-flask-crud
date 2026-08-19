from flask import Flask, request, jsonify
from models.tasks import Task

app = Flask(__name__)

#CRUD

#CREATE
#READ
#UPTADE
#DELETE

tasks = []
taskIDcontrol = 1

@app.route('/tasks', methods=['POST'])
def createTask():
    global taskIDcontrol
    data = request.get_json()
    newTask = Task(
    id=taskIDcontrol,
    title=data.get("title", ""),
    description=data.get("description", "")
)
    taskIDcontrol += 1 
    tasks.append(newTask)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso."})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    taskList = []
    for task in tasks:
        taskList.append(task.to_dict())
    output = {
                "tasks": taskList,
                "total_tasks": len(taskList)

                }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
        
    return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404


#UPDATE

@app.route('/tasks/<int:id>', methods = ['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t 
    print(task)

    if task == None:
        return jsonify ({"message": "Não foi possivel encontrar a atividade"}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso!"})

#DELETE

@app.route('/tasks/<int:id>', methods = ['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break


    if not task:
        return jsonify({"message":"Não foi possivel encontrar a atividade"}), 404

    tasks.remove(task)
    return jsonify({"message":"Tarefa deletada com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)