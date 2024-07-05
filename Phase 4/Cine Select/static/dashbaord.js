$(document).ready(function() {
    // Replace 'YOUR_API_KEY' with your actual API key
    var myAPI = '1f0ab2203ed8bd14183d3f233a84e18d';

    // Function to fetch latest movies
    function fetchLatestMovies() {
        var url = 'https://api.themoviedb.org/3/discover/movie?api_key=' + myAPI + '&sort_by=release_date.desc';

        $.ajax({
            type: 'GET',
            url: url,
            success: function(data) {
                var movies = data.results.slice(0, 5); // Limiting to 5 latest movies
                var movieListHtml = '';

                movies.forEach(function(movie) {
                    var posterPath = movie.poster_path ? 'https://image.tmdb.org/t/p/original' + movie.poster_path : '/static/default.jpg';
                    movieListHtml += '<div class="movie">';
                    movieListHtml += '<img src="' + posterPath + '" alt="' + movie.title + '">';
                    movieListHtml += '<div class="movie-details">';
                    movieListHtml += '<h3>' + movie.title + '</h3>';
                    movieListHtml += '<p>' + movie.release_date + '</p>';
                    movieListHtml += '</div></div>';
                });

                $('#latest-movies-list').html(movieListHtml);
            },
            error: function(xhr, status, error) {
                console.error('Error fetching latest movies:', error);
            }
        });
    }

    // Fetch latest movies on page load
    fetchLatestMovies();
});
