<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="Content-type" name="viewport" content="initial-scale=1.0, maximum-scale=1.0, user-scalable=no, width=device-width">
        <link rel="stylesheet" href="css/main.css">
        <script src="http://code.jquery.com/jquery-1.11.2.min.js"></script>
        <script src="//use.edgefonts.net/source-sans-pro:n3,n4,n6;source-code-pro:n3.js"></script>
        <script src="https://google-code-prettify.googlecode.com/svn/loader/run_prettify.js"></script>
        <script type="text/javascript">
            $(document).ready(function(){
                $('#regularFeed').click(function(){
                    var a = new XMLHttpRequest();
                    a.open("GET","regularFeed.php");
                    a.onreadystatechange=function(){
                        if(a.readyState==4){
                            if(a.status == 200){
                            }
                            else alert("HTTP ERROR");
                        }
                    }
                    a.send();
                });
            $('#largeFeed').click(function(){
                    var a = new XMLHttpRequest();
                    a.open("GET","largeFeed.php");
                    a.onreadystatechange=function(){
                        if(a.readyState==4){
                            if(a.status == 200){
                            }
                            else alert("HTTP ERROR");
                        }
                    }
                    a.send();
                });
            $('#unjam').click(function(){
                    var a = new XMLHttpRequest();
                    a.open("GET","unjam.php");
                    a.onreadystatechange=function(){
                        if(a.readyState==4){
                            if(a.status == 200){
                            }
                            else alert("HTTP ERROR");
                        }
                    }
                    a.send();
                });
            });
        </script>
        <title>Cat Feeder</title>
    </head>
    <body>
        <center>
        <button type="button" id="regularFeed" class="topcoat-button">Regular Feeding</button><br><br>
        <button type="button" id="largeFeed" class="topcoat-button">Large Feeding</button><br><br>
        <button type="button" id="unjam" class="topcoat-button">Unjam Feeder</button><br><br>
        <button onclick="window.location.href='feedings.log'" type="button" id="feedlog" class="topcoat-button">View Feeding Log</button>
        <center>
    </body>
</html>