# python-fire-example

```
pipenv --python 3.10
```

# Install pip packages included dev-dependencies

```
pipenv sync -dev
```

# scripts

## lint

```
pipenv run lint
```

## run

```
pipenv run start
```

## calc-instance
```
> pipenv run start calc-instance double 2
Loading .env environment variables...
4
```

## calc-class
```
> pipenv run start calc-class double 2
Loading .env environment variables...
4
```

## calc-instance
```
```

## hello

```
> pipenv run start hello xxx
Loading .env environment variables...
Hello xxx!
```

## os

```
> pipenv run start os environ get --key="ENV"
Loading .env environment variables...
DEBUG
```
## env

```
> pipenv run start env get_env --key="ENV"   
Loading .env environment variables...
DEBUG
```