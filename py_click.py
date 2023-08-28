import click;
import json_manager

# adding the prinsipal command
@click.group()
def cli ():
  pass 

#by adding the subcommands and options
@cli.command()
@click.option('--name', required=True, help='Name of the user')
@click.option('--lastname', required=True, help='lastname of the user')
@click.pass_context
def newUser (ctx, name, lastname):
  if not name or not lastname:
    ctx.fail('The name and lastaname are required')

  else:
    data = json_manager.redJson()
    userId = len(data) + 1
    
    user = {
      'id': userId,
      'name': name,
      'lastname': lastname,
    }

    data.append(user)
    json_manager.writeJson(data) 

    # return f'User {name} {lastname} created successfully with id {userId}'
    print(f'User {name} {lastname} created successfully with id {userId}')

@cli.command()
@click.argument('id', required=True, type=int)
def getUser(id):
  users = json_manager.redJson()
  user = next((user for user in users if user['id'] == id), None)

  if user == None: print(f'User with id {id} not found')

  else: print(f'User {user["name"]} {user["lastname"]} id {user["id"]}')

@cli.command()
def users ():
  users = json_manager.redJson()
  dataUsers = ''
  
  for user in users:
    dataUsers += f'{user["name"].title()} {user["lastname"].title()} id {user["id"]} \n'

  print(dataUsers)  

@cli.command()
@click.argument('id', required=True, type=int)
def deleteUser (id):
  users = json_manager.redJson()
  user = next((user for user in users if user['id'] == id), None)

  if user is None:
    print(f'User with id ({id}) not found')

  else:
    users.remove(user)
    json_manager.writeJson(users)
    print(f'User with id ({id}) delete successfully')

@cli.command() 
@click.argument('id', type=int)
@click.option('--name', required=True, help='The name is required')
@click.option('--lastname', required=True, help='The lastname is required')
def userUpdate (id, name, lastname):  
  users = json_manager.redJson()

  for user in users:
    if user['id'] == id:
      if name is not None:
        user['name'] = name

      if lastname is not None:    
        user['lastname'] = lastname
      break  

  json_manager.writeJson(users)
  print(f'User with id ({id}) update successfully')
  
if __name__ == '__main__':
  cli()

