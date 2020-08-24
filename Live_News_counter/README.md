# News Live Count Scrapping

Uses selenium so it needs a webdriver and it shall be downloaded and path shall be given in main python or add to $PATH.
```shell
python3 main.py
```
This command will start to scrap YT major news channels like

> Asianet News
>
> News24
>
> Manorma
>
> MediaOne

The Data will be saved in a csv file and will be displayed in the browser by running streamlit App.

```shell
streamlit run app.py
```



## To Do
> Multi threading for the scraping to make it faster
>
> Migrate to firefox for scrapping | Urlllib is not working as count is loaded in JS in browser or need to find a work around
>
> Date mangment in streamlit
