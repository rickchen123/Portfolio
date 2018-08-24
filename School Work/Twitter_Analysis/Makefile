#Setting up enviroment
ENV_YML=environment.yml

.PHONY : env
env : $(ENV_YML)
	conda env create -f $(ENV_YML)
#Running all notebooks
.PHONY : all
all:
	jupyter nbconvert --ExecutePreprocessor.timeout=3600 --to notebook --execute Notebook1
	jupyter nbconvert --ExecutePreprocessor.timeout=3600 --to notebook --execute Notebook2
	jupyter nbconvert --ExecutePreprocessor.timeout=3600 --to notebook --execute Notebook 3
	jupyter nbconvert --ExecutePreprocessor.timeout=3600 --to notebook --execute Notebook 4
	jupyter nbconvert --ExecutePreprocessor.timeout=3600 --to notebook --execute main.ipynb

.PHONY: test
test: #runs as expected
	python tests.py

#Create a phony clean target to remove saved variables and figures
.PHONY : clean
clean:
	rm -f fig/*.png
	rm -f fig/*.html
	rm -f result/*.h5
	rm -f result/*.bak
	rm -f result/*.dat
	rm -f result/*.db
	rm -f result/*.dir