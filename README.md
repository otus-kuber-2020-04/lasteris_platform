# Выполнено ДЗ № 1

 - [x] Основное ДЗ
 - [ ] Задание со *

## В процессе сделано:
 - Установлены minikube, kubectl, bash-completion
 - Проверена устойчивость к отказам.
 - Создано простое webapp, развернут образ с помощью Dockerfile и добавлено в DockerHub в репозиторий
 lasteris/web с тегом 1.0
 - Склонировано микросервис HipsterShop. Развернут образ с помощью существующего в нем же Dockerfile'а в репозиторий lasteris/frontend:1.0
 - создан файл конфигурации web-pod.yaml
 - сгенерирован файл конфигурации frontend-pod.yaml

## Почему при удалении pod'ов все восстановилось ?
Выполним команду: kubectl describe pods --all-namespaces
и посмотрим :)
core-dns: Controlled By ReplicaSet/core-dns-<replica-set-id>
Как я понял, за core-dns следит Deployment Controller (соответственно необходимо удалить deployment, а не pod),
опираясь на файл manifest'а. Если значение replica становится ниже 2, то создается ReplicaSet (core-dns-<replica-set-id>).
Далее ReplicaSet создает pod (core-dns-<replica-set-id>-<pod-id>).
kube-proxy: Controlled By DaemonSet/kube-proxy
DaemonSet следит за тем, чтобы pod'ы, находящиеся под его юрисдикцией были запущены на каждой машине.
Соответственно, когда добавляется новая node'а, DaemonSet создает там соответствующий pod.
kube-scheduler-minikube, kube-controller-manager-minikube, etcd-minikube, kube-apiserver-minikube (тут можно догадаться уже из постфикса):
Controlled By: Node/minikube
Это 'static pods' необходимые для самонастройки рабочего окружения. Управляются напрямую kubelet-агентом.
storage-provisioner, в первую очередь, является аддоном, поэтому он не восстановился.

## Как тестировал docker-образ:
 1.  docker run -it -p 8000:8000 lasteris/flask-basic:0.1
 2. curl localhost:8080/ и получить html вывод

## Как запустить и протестировать pod:
 - kubectl apply -f web-pod.yaml
 - kubectl port-forward --address 0.0.0.0 pod/web 8000:8000