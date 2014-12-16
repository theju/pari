(function() {
    var sc = document.createElement("script");
    function cb(data) {
	var holder = document.getElementById(__pariAlbum.widgetId);
	holder.innerHTML = data.html;
    }
    window.pariAlbumParseResponse = cb;
    sc.src = "//pari.tld/albums/talking/embed/?url=" + encodeURIComponent(__pariAlbum.url)
	+  "&width=" + __pariAlbum.widgetWidth
	+  "&height=" + __pariAlbum.widgetHeight +
	"  &&callback=pariAlbumParseResponse";
    document.body.appendChild(sc);
})();
