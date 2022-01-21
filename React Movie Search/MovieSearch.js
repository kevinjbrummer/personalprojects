import React, {useState} from "react";
import "./style.css";
import MovieCard from "./movieCard.js";

export default function SearchMovies() {
    const [query, setQuery] = useState('');
    const [movies, setMovies] = useState([]);

    const searchMovies = async(e) => {
        e.preventDefault();


        const url = `https://api.themoviedb.org/3/search/movie?api_key=16288ce40f46c195be862b0263631c93&query=${query}&language=ja&region=ja`;

        try{
            const res = await fetch(url);
            const data = await res.json();
            setMovies(data.results);
        }catch(err){
            console.error(err);
        }
    }
 

    return(
        <>
            <form className="form" onSubmit={searchMovies}>
                <label className="label" htmlFor="query" >
                    映画名:
                </label>
                <input className="input" type="text" name="query"
                placeholder="例：となりのトトロ"
                value={query} onChange={(e) => setQuery(e.target.value)}
                >
                </input>
                <button className="button" type="submit">
                    検索
                </button>
            </form>

            <div className="card-list">
            {movies.filter(movie => movie.poster_path).map(movie => 
                <MovieCard movie={movie}  key={movie.id}></MovieCard>)}
            </div>
        </>
    )
}