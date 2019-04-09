$( document ).ready(function() {
    var mapPopUp = null;
    var osm = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var gm = 'https://maps.googleapis.com/maps/vt?pb=!1m5!1m4!1i{z}!2i{x}!3i{y}!4i256!2m3!1e0!2sm!3i349018013!3m9!2sen-US!3sUS!5e18!12m1!1e47!12m3!1e37!2m1!1ssmartmaps!4e0';
    /*-------------------------------------------
        PopUp Map 
    -------------------------------------------*/
    // event single
    $('.lc-event-single [data-toggle="modal"]').on('click', function (e) {
        var data = $(e.target).closest('div.lc-event-single').data();
        jQuery('.lc-listing-modal').on('shown.bs.modal', function (e) {
            // call map function
            lcPopUpMap({
                'lat'           : data.lat,
                'lng'           : data.lng,
                'maptype'       : data.maptype,
                'marker_url'    : data.marker,
            });
        });
    });
    // for lisitng single
    $('.lc-listing-single [data-toggle="modal"]').on('click', function (e) {
        var data = $(e.target).closest('div.lc-listing-single').data();
        jQuery('.lc-listing-modal').on('shown.bs.modal', function (e) {
            // call map function
            lcPopUpMap({
                'lat'           : data.lat,
                'lng'           : data.lng,
                'maptype'       : data.maptype,
                'marker_url'    : data.marker,
            });
        });
    });
    // contact widget map
    $('.widget-about-launch-map').on('click', function (e) {
        var data = $(e.target).data();
        jQuery('#lc-widget-popup-location').on('shown.bs.modal', function (e) {
            // insert map html
            $('.lc-popup-map-view').html('<div id="lc-popup-map"></div>');
            // call map function
            lcPopUpMap({
                'lat'           : data.lat,
                'lng'           : data.lng,
                'maptype'       : data.maptype,
                'marker_url'    : data.marker,
            });
        });
    });
    // remove map html
    
    // common function
    var lcPopUpMap = function (mapObj){
        var container = L.DomUtil.get('lc-popup-map');
          if(container != null){
            container._leaflet_id = null;
          }
        // map init
        mapPopUp = L.map('lc-popup-map', {
            center: [45, 10],
            zoom: 4,
        });
        if(mapObj.maptype == 'osm'){    // open street map
            L.tileLayer(osm).addTo(mapPopUp);
        } else {                // google map
            L.tileLayer(gm).addTo(mapPopUp); 
        }
        var lcIcon = L.icon({   // Custom Icon  
            iconUrl: mapObj.marker_url,
            iconSize: [41, 49], // size of the icon
        }); 
        var marker = L.marker([mapObj.lat, mapObj.lng], {icon: lcIcon}).addTo(mapPopUp);
        mapPopUp.setView(new L.LatLng(mapObj.lat, mapObj.lng), 8)
    }


    $('.lc-listing-modal').on('hidden.bs.modal', function () {
        if(mapPopUp !== undefined || mapPopUp !== null) {
          mapPopUp.remove(); 
       }
    });


    /*-------------------------------------------
        basic map
    -------------------------------------------*/
    // contact map
    if($('#lc-map-contact').length > 0){
        var basicMapData = $('#lc-map-contact').data();
        lcBasicMap({
            'id'            : 'lc-map-contact',
            'lat'           : basicMapData.lat,
            'lng'           : basicMapData.lng,
            'zoom'          : basicMapData.zoom,
            'maptype'       : basicMapData.maptype,
            'marker_url'    : basicMapData.marker,
        });
    }
    if($('#lc-listing-details-map').length > 0){
        var basicMapData = $('#lc-listing-details-map').data();
        lcBasicMap({
            'id'            : 'lc-listing-details-map',
            'lat'           : basicMapData.lat,
            'lng'           : basicMapData.lng,
            'zoom'          : basicMapData.zoom,
            'maptype'       : basicMapData.maptype,
            'marker_url'    : basicMapData.marker,
        });
    }
    function lcBasicMap(mapObj){
        var container = L.DomUtil.get(mapObj.id);
          if(container != null){
            container._leaflet_id = null;
          }
        // map init
        mapPopUp = L.map(mapObj.id, {
            center: [45, 10],
            zoom: mapObj.zoom,
        });
        if(mapObj.maptype == 'osm'){    // open street map
            L.tileLayer(osm).addTo(mapPopUp);
        } else {                // google map
            L.tileLayer(gm).addTo(mapPopUp); 
        }
        var lcIcon = L.icon({   // Custom Icon  
            iconUrl: mapObj.marker_url,
            iconSize: [41, 49], // size of the icon
        }); 
        var marker = L.marker([mapObj.lat, mapObj.lng], {icon: lcIcon}).addTo(mapPopUp);
        mapPopUp.setView(new L.LatLng(mapObj.lat, mapObj.lng), 8)
    }
    
    /*-------------------------------------------
        search map
    -------------------------------------------*/
    var searchMap = function(mapObj){
        // L.Icon extend
        L.HtmlIcon = L.Icon.extend({
          options: {},

          initialize: function (options) {
            L.Util.setOptions(this, options);
          },

          createIcon: function () {
            var div = document.createElement('div');
            div.innerHTML = this.options.html;
            return div;
          },

          createShadow: function () {
            return null;
          }
        });
        // L.Icon extend
        var currentType = '';
        if(mapObj.maptype == 'osm'){
            currentType = osm;
        } else {
            currentType = gm;
        }
        var tiles = L.tileLayer(currentType, {maxZoom: 18});
        var latlng = L.latLng(mapObj.lat, mapObj.lng);

        var map = L.map(mapObj.id, {center: latlng, scrollWheelZoom: false, zoom: mapObj.zoom, layers: [tiles]});

        var markers = L.markerClusterGroup({
            scrollWheelZoom: false,
            showCoverageOnHover: false,
            maxClusterRadius: 10,
            iconCreateFunction : function (cluster) {
                return L.divIcon( {
                    html : '<div class="markerclusergroupicon"><img src="images/marker/cluster.png" alt="marker"><span class="number">' + cluster.getChildCount() + '</span><div>', 
                    className : 'mycluster',
                });
            }
        });
        
        for (var i = 0; i < addressPoints.length; i++) {
            var a = addressPoints[i];
            var title = a[2];
            // non  extender 
            // var lcIcon = L.icon({   // Custom Icon  
            //     iconUrl: (a[3] !='' ? a[3] : mapObj.marker_url),
            //     iconSize: [38, 95], // size of the icon
            //     iconID: a[4]
            // }); 

            // extender icon
            var lcIcon = new L.HtmlIcon({
              html: "<div class='lc-marker lc-map-marker" + a[4] + "' data-markerid=" + a[4] + " style='margin-top: -50px;margin-left: -20px;'><img src='" + (a[3] !='' ? a[3] : mapObj.marker_url) + "' alt='icon' /></div>",
              markerid: a[4],
            });
            // 
            markers.on('clusterclick', function () {
              var lcIcon = new L.HtmlIcon({
                html: "<div class='lc-marker lc-map-marker" + a[4] + "' data-markerid=" + a[4] + " style='margin-top: -50px;margin-left: -20px;'><img src='" + (a[3] !='' ? a[3] : mapObj.marker_url) + "' alt='icon' /></div>",
                markerid: a[4],
              });
            });


            var marker = L.marker(new L.LatLng(a[0], a[1]), {  icon: lcIcon, markerID: a[4] });
            marker.bindPopup(title);
            markers.addLayer(marker);
        }

        map.addLayer(markers);


        // console.log(markers._topClusterLevel.getAllChildMarkers());
        // Mouse Hover Effect for bounce
        if (jQuery('.lc-search-map-content .lc-listing-single') != null){
          jQuery('.lc-search-map-content .lc-listing-single').on('mouseover', function () {
            for (var k = 0; k < addressPoints.length; k++) {
              var allMarkers = markers._topClusterLevel.getAllChildMarkers();
              var markarPostId = allMarkers[k].options.icon.options.markerid;
              if (markarPostId == jQuery(this).data('postid')) {
                jQuery(".lc-map-marker" + markarPostId).addClass('activated');
              } else {
                jQuery(".lc-map-marker" + markarPostId).removeClass('activated');
              }
            }
          });
        }

        // scroll no off map
        $('#'+mapObj.id).append(' <a href="#" id="mapScrollEnabling" class="btn btn-map-scroll enabled"><span class="ti-mouse"></span>Enable Scrolling</a> ');
        $('#mapScrollEnabling').on('click', function(e){
            e.preventDefault();
            $(this).toggleClass("enabled");
            if($(this).is(".enabled")) {
               map.scrollWheelZoom.disable()
            }
            else {
                map.scrollWheelZoom.enable()
            }
        });
    }
    if($('#lc-search-map').length){
        var searchMapType = $('#lc-search-map').data();
        searchMap({
            'id'            : 'lc-search-map',
            'lat'           : searchMapType.lat,
            'lng'           : searchMapType.lng,
            'zoom'          : searchMapType.zoom,
            'maptype'       : searchMapType.maptype,
            'marker_url'    : searchMapType.marker,
        });
    }

    if($('#home-3-map').length){
        var searchMapType = $('#home-3-map').data();
        searchMap({
            'id'            : 'home-3-map',
            'lat'           : searchMapType.lat,
            'lng'           : searchMapType.lng,
            'zoom'          : searchMapType.zoom,
            'maptype'       : searchMapType.maptype,
            'marker_url'    : searchMapType.marker,
        });
    }

    /*-------------------------------------------
        Fake Notification
    -------------------------------------------*/
    var lcFakeNotification = function(){
        $('div.lc-fake-notification div.lc-msg').css({
            "position" : "absolute",
            "top"  : "0",
            "right": "300px"
        });
        $('div.lc-fake-notification div.lc-msg:nth-child(2)').css({
            "position" : "absolute",
            "top"  : "60px",
            "right": "50px"
        });
        $('div.lc-fake-notification div.lc-msg:nth-child(3)').css({
            "position" : "absolute",
            "top"  : "140px",
            "right": "200px"
        });
        $('div.lc-fake-notification div.lc-msg:nth-child(4)').css({
            "position" : "absolute",
            "top"  : "100px",
            "left": "100px"
        });
        $('div.lc-fake-notification div.lc-msg:nth-child(5)').css({
            "position" : "absolute",
            "top"  : "300px",
            "left": "95px"
        });
        $('div.lc-fake-notification div.lc-msg:nth-child(6)').css({
            "position" : "absolute",
            "top"  : "350px",
            "right": "0"
        });
        
        // var list = [1, 2, 3, 4, 5];

        var i = 0;
        var intervalId = setInterval(function(){
           if(i === 6){
              // clearInterval(intervalId);
              i = 0;
           }
         
            $('div.lc-fake-notification div.lc-msg:nth-child('+i+')').addClass('active');
            $('div.lc-fake-notification div.lc-msg:nth-child('+i+') .popup').append('<div class="info"><b>John</b> Create A list</div>')


           i++;
        }, 1000);

        var k = 0;
        var TimeoutId = function(){ setInterval(function(){
               if(k === 6){
                  // clearInterval(intervalId);
                  k = 0;
               }
                $('div.lc-fake-notification div.lc-msg:nth-child('+k+')').removeClass('active');
                $('div.lc-fake-notification div.lc-msg:nth-child('+k+') .popup').empty();

               k++;
            }, 1000);
        }

        setTimeout(TimeoutId, 5000)

    }
    lcFakeNotification();



    // geo search
    if($('#cpdl-map').length > 0) {
        var mapType = $('#cpdl-map').data();
        if(mapType.type == 'osm'){
            openStreetGeoSearch();
        }else {
            googleGeoSearch();
        }
    }



   /*
    |-----------------------------------------
    | Open Street Search
    |------------------------------------------
    */
    function openStreetGeoSearch(){
        /* Initialize basic map */
        var map = L.map('cpdl-map').setView([52.0852378,5.3846249], 9);
        L.tileLayer(
            'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            }).addTo(map);

            /* Create searchcontrols */

            var GeoSearchControl = window.GeoSearch.GeoSearchControl;
            var OpenStreetMapProvider = window.GeoSearch.OpenStreetMapProvider;
            var provider = new OpenStreetMapProvider({});

            //  Define search controls
            var searchControl = new GeoSearchControl({
                provider: provider,
                style: 'bar',
                showMarker: true,
                marker: {
                    draggable: true
                },
                autoClose: true,
                keepResult: true,
            });
            
            // Add searchbar to the map
            map.addControl(searchControl);

            /* Create new layer for markers  */
            map.on('geosearch/showlocation', function(e) {
                $('#listing_address').val(e.location.label);
                $("#lat").val(e.location.y);
                $("#lng").val(e.location.x);
                // add marker
                var markers = L.markerClusterGroup();
                var lcIcon = L.icon({   // Custom Icon  
                    iconUrl: 'images/logo.png',
                    iconSize: [38, 95], // size of the icon
                }); 
                var marker = L.marker(new L.LatLng(e.location.y, e.location.x), { title: e.location.label, icon: lcIcon });
                marker.bindPopup(e.location.label);
                markers.addLayer(marker);
                map.addLayer(markers);
            });

        /*map.on('click', function(e) {
            var newMarker = new L.marker(e.latlng).addTo(map);
            $("#lat").val(e.location.y);
            $("#lng").val(e.location.x);

            });
        */
        map.on('geosearch/marker/dragend', function(e) {
            $('#listing_address').val(e.location.label);
            $("#lat").val(parseFloat(e.location.lat));
            $("#lng").val(parseFloat(e.location.lng));
        });

        
    }
    /*
    |-----------------------------------------
    | Google Geo Search
    |------------------------------------------
    */
    function googleGeoSearch() {

        var markers = [];
        var map = new google.maps.Map(document.getElementById('cpdl-map'), {
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            // center: {lat: 40.674, lng: -73.945},
            center: {lat: 6.6039262, lng: 3.3327518},
            zoom: 10,
            mapTypeControl: true,
            mapTypeControlOptions: {
                style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR,
                position: google.maps.ControlPosition.BOTTOM_CENTER
            },
            zoomControl: true,
            zoomControlOptions: {
                position: google.maps.ControlPosition.LEFT_BOTTOM
            },
            scaleControl: true,
            streetViewControl: true,
            streetViewControlOptions: {
                position: google.maps.ControlPosition.RIGHT_BOTTOM
            },
            fullscreenControl: false,
            styles: [
                {
                    "featureType": "water",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "color": "#e9e9e9"
                        },
                        {
                            "lightness": 17
                        }
                    ]
                },
                {
                    "featureType": "landscape",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "color": "#f5f5f5"
                        },
                        {
                            "lightness": 20
                        }
                    ]
                },
                {
                    "featureType": "road.highway",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#ffffff"
                        },
                        {
                            "lightness": 17
                        }
                    ]
                },
                {
                    "featureType": "road.highway",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        {
                            "color": "#ffffff"
                        },
                        {
                            "lightness": 29
                        },
                        {
                            "weight": 0.2
                        }
                    ]
                },
                {
                    "featureType": "road.arterial",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "color": "#ffffff"
                        },
                        {
                            "lightness": 18
                        }
                    ]
                },
                {
                    "featureType": "road.local",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "color": "#ffffff"
                        },
                        {
                            "lightness": 16
                        }
                    ]
                },
                {
                    "featureType": "poi",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "color": "#f5f5f5"
                        },
                        {
                            "lightness": 21
                        }
                    ]
                },
                {
                    "featureType": "poi.park",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "color": "#dedede"
                        },
                        {
                            "lightness": 21
                        }
                    ]
                },
                {
                    "elementType": "labels.text.stroke",
                    "stylers": [
                        {
                            "visibility": "on"
                        },
                        {
                            "color": "#ffffff"
                        },
                        {
                            "lightness": 16
                        }
                    ]
                },
                {
                    "elementType": "labels.text.fill",
                    "stylers": [
                        {
                            "saturation": 36
                        },
                        {
                            "color": "#333333"
                        },
                        {
                            "lightness": 40
                        }
                    ]
                },
                {
                    "elementType": "labels.icon",
                    "stylers": [
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "transit",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "color": "#f2f2f2"
                        },
                        {
                            "lightness": 19
                        }
                    ]
                },
                {
                    "featureType": "administrative",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#fefefe"
                        },
                        {
                            "lightness": 20
                        }
                    ]
                },
                {
                    "featureType": "administrative",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        {
                            "color": "#fefefe"
                        },
                        {
                            "lightness": 17
                        },
                        {
                            "weight": 1.2
                        }
                    ]
                }
            ]
        });
        $('#cpdl-map').append(' <input id="pac-input" class="form-control controls" type="text" placeholder="Search Box">');
        // Create the search box and link it to the UI element.
        var input = document.getElementById('pac-input');
        var searchBox = new google.maps.places.SearchBox(input);
        map.controls[google.maps.ControlPosition.TOP].push(input);

        // Bias the SearchBox results towards current map's viewport.
        map.addListener('bounds_changed', function() {
          searchBox.setBounds(map.getBounds());
        });

        var markers = [];
        // Listen for the event fired when the user selects a prediction and retrieve
        // more details for that place.
        searchBox.addListener('places_changed', function() {
          var places = searchBox.getPlaces();

          if (places.length == 0) {
            return;
          }

          // Clear out the old markers.
          markers.forEach(function(marker) {
            marker.setMap(null);
          });
          markers = [];

          // For each place, get the icon, name and location.
          var bounds = new google.maps.LatLngBounds();
          places.forEach(function(place) {
            if (!place.geometry) {
              console.log("Returned place contains no geometry");
              return;
            }
            var icon = {
              url: place.icon,
              size: new google.maps.Size(71, 71),
              origin: new google.maps.Point(0, 0),
              anchor: new google.maps.Point(17, 34),
              scaledSize: new google.maps.Size(25, 25)
            };

            // Create a marker for each place.
            markers.push(new google.maps.Marker({
              map: map,
              icon: icon,
              title: place.name,
              position: place.geometry.location
            }));

            $('#listing_address').val(place.formatted_address);
            $("#lat").val(parseFloat(place.geometry.location.lat()));
            $("#lng").val(parseFloat(place.geometry.location.lng()));

            if (place.geometry.viewport) {
              // Only geocodes have viewport.
              bounds.union(place.geometry.viewport);
            } else {
              bounds.extend(place.geometry.location);
            }
          });
    
            // map.fitBounds(bounds);

            
        });
    }    
});