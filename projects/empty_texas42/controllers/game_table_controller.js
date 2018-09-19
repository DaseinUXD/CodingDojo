// Export functions for our routes.js file to use. This is where the logic of
// your server will go.
module.exports = {
    
    set_players: function (req, res) {
        // A dummy array of users.
        var players_array = [
            {name: ''},
            {name: ''},
            {name: ''},
            {name: ''}
        ];
        
        // In order to display a page with data we need to render. The first argument
        // render needs is the file. Here, it is index.ejs. Express knows where to find
        // this file because in server.js we told express where our views are
        // (line 14).
        
        // Next, render needs an object. The key, or property in this object will be
        // the name we can use in our ejs file ('users' here) and the value will
        // be what is stored in that property (the users_array from above).
        res.render('game_table', {all_players: players_array});
    }
    
    chat_message: function (request, response) {
        res.redirect('game_table')
    }
    
};
