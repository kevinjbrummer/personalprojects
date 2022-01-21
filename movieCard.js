import React from "react";

export default function MovieCard({movie}){
    return(
        <div className="card">
            <img className="card--image"
                src={`https://image.tmdb.org/t/p/w185_and_h278_bestv2/${movie.poster_path}`}
                alt={movie.title + " poster"}>
            </img>

            <div className="card--content">
                <h3 className="card--title">
                    {movie.title}
                </h3>
                <p><small>公開: {movie.release_date}
                </small></p>
                <p><small>評価: {movie.vote_average}
                </small></p>
                <p className="card-description">
                    {movie.overview}
                </p>
            </div>
        </div>
    )
}