# medicalsys


# Run application

```
docker-compose up --build
```

# Após a inicialização com o comando, precisa criar o super usuario em outra bash para ter acesso as páginas

# Create SuperUser
```
docker-compose exec app python manage.py createsuperuser
```

# Feito os passo acima é so testar a aplicação