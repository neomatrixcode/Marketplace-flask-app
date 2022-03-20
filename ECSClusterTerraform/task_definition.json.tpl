[
    {
        "essential": true,
        "memory": 512,
        "name": "worker",
        "cpu": 2,
        "image": "${REPOSITORY_URL}:latest",
        "environment": [
    "DATABASE_URL"= ${var.mysql.engine}://${var.mysql.username}:${var.mysql.password}@${aws_db_instance.mysql.endpoint}:${var.mysql.port}/${var.mysql.name}
  ]
    }
]