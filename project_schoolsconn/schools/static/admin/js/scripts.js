(function($) {
    "use strict";
    $(document).ready(function() {

        /* -----------------------------------------------------
            Navbar
        ----------------------------------------------------- */
        $( "#lcdnavbar" ).superMegaMenu();

        /*==Left Navigation Accordion ==*/
        if ($.fn.dcAccordion) {
            $('#lcd-nav-accordion').dcAccordion({
                eventType: 'click',
                autoClose: true,
                saveState: true,
                disableLink: true,
                speed: 'slow',
                showCount: false,
                autoExpand: true,
                classExpand: 'dcjq-current-parent'
            });
        }

        $('.lcd-sidebar-toggle-box span').click(function (e) {
            $('#lcd-sidebar').toggleClass('lcd-hide-left-bar');
            $('#lcdnavbar').toggleClass('lcd-hide-nav-bar');
            $('#lcd-sidebar ul li').toggleClass('lcd-hide-nav-bar');
            $('.lcd-leftside-navigation ul.lcd-sidebar-menu li a').toggleClass('active');
            $('.lcd-leftside-navigation ul.lcd-sidebar-menu li ul.sub').css({"display": "none"});
            /* right-sitebar */
            $('#lcd-main-content').toggleClass('lcd-merge-left');
            e.stopPropagation();
            if ($('#container').hasClass('open-right-panel')) {
                $('#container').removeClass('open-right-panel')
            }
            if ($('.right-sidebar').hasClass('open-right-bar')) {
                $('.right-sidebar').removeClass('open-right-bar')
            }
            if ($('.lcd-header-area').hasClass('merge-header')) {
                $('.lcd-header-area').removeClass('merge-header')
            }
        });
        $('.lcd-leftside-navigation ul.lcd-sidebar-menu li a').click(function (e) {
            $('#lcd-sidebar').removeClass('lcd-hide-left-bar');
            $('#lcd-main-content').removeClass('lcd-merge-left');
        });


       

        /*------------------------------------------------------------------
            ChartOne
        -------------------------------------------------------------------*/
        $("#lcd-panel-review-chart").on("inview",function(){
            var ctx = document.getElementById('lcd-panel-review-chart').getContext("2d");
                var gradientStroke = ctx.createLinearGradient(0, 0, 0, 450);
                gradientStroke.addColorStop(0, '#f55f41');
                gradientStroke.addColorStop(1, '#f55f41');

                var gradientFill = ctx.createLinearGradient(0, 0, 0, 450);
                gradientFill.addColorStop(0, "rgba(245,93,62,0.1)");
                gradientFill.addColorStop(1, "rgba(245,93,62,0)");

                // datasets 2
                var gradientStroke2 = ctx.createLinearGradient(0, 0, 0, 450);
                gradientStroke2.addColorStop(0, '#1580c8');
                gradientStroke2.addColorStop(1, '#1580c8');

                var gradientFill2 = ctx.createLinearGradient(0, 0, 0, 450);
                gradientFill2.addColorStop(0, "rgba(243,167,18,0.1)");
                gradientFill2.addColorStop(1, "rgba(243,167,18,0)");

                // datasets 3
                var gradientStroke3 = ctx.createLinearGradient(0, 0, 0, 450);
                gradientStroke3.addColorStop(0, '#00d27a');
                gradientStroke3.addColorStop(1, '#00d27a');

                var gradientFill3 = ctx.createLinearGradient(0, 0, 0, 450);
                gradientFill3.addColorStop(0, "rgba(241,167,18,0.1)");
                gradientFill3.addColorStop(1, "rgba(241,167,18,0)");

                // datasets 4
                var gradientStroke4 = ctx.createLinearGradient(0, 0, 0, 450);
                gradientStroke4.addColorStop(0, '#9e5eff');
                gradientStroke4.addColorStop(1, '#9e5eff');

                var gradientFill4 = ctx.createLinearGradient(0, 0, 0, 450);
                gradientFill4.addColorStop(0, "rgba(241,167,18,0.1)");
                gradientFill4.addColorStop(1, "rgba(241,167,18,0)");

                // datasets 4
                var gradientStroke5 = ctx.createLinearGradient(0, 0, 0, 450);
                gradientStroke5.addColorStop(0, '#f3a712');
                gradientStroke5.addColorStop(1, '#f3a712');

                var gradientFill5 = ctx.createLinearGradient(0, 0, 0, 450);
                gradientFill5.addColorStop(0, "rgba(241,167,18,0.1)");
                gradientFill5.addColorStop(1, "rgba(241,167,18,0)");

                // all data
                var temp_dataset = [0, 0, 2, 5, 16, 25, 30, 35, 45];
                var rain_dataset = [4100, 5000, 4200, 4400, 4800, 4600, 4800, 4600, 4300];
                var temp_lavels = ["", "", "", "", "", "", "","", ""];

                var myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: temp_lavels,
                        datasets: [{
                            label: "Data",
                            borderColor: gradientStroke,
                            pointBorderColor: gradientStroke,
                            pointBackgroundColor: gradientStroke,
                            pointHoverBackgroundColor: gradientStroke,
                            pointHoverBorderColor: gradientStroke,
                            pointBorderWidth: 1,
                            pointHoverRadius: 1,
                            pointHoverBorderWidth: 1,
                            pointRadius: 1,
                            fill: true,
                            backgroundColor: gradientFill,
                            borderWidth: 1,
                            data: temp_dataset
                        },
                        {
                            label: "Data",
                            borderColor: gradientStroke2,
                            pointBorderColor: gradientStroke2,
                            pointBackgroundColor: gradientStroke2,
                            pointHoverBackgroundColor: gradientStroke2,
                            pointHoverBorderColor: gradientStroke2,
                            pointBorderWidth: 1,
                            pointHoverRadius: 1,
                            pointHoverBorderWidth: 1,
                            pointRadius: 1,
                            fill: true,
                            backgroundColor: gradientFill2,
                            borderWidth: 1,
                            data: [10, 14, 25, 35, 40, 39, 50, 55, 60]
                        },
                        {
                            label: "Data",
                            borderColor: gradientStroke3,
                            pointBorderColor: gradientStroke3,
                            pointBackgroundColor: gradientStroke3,
                            pointHoverBackgroundColor: gradientStroke3,
                            pointHoverBorderColor: gradientStroke3,
                            pointBorderWidth: 1,
                            pointHoverRadius: 1,
                            pointHoverBorderWidth: 1,
                            pointRadius: 1,
                            fill: true,
                            backgroundColor: gradientFill3,
                            borderWidth: 1,
                            data: [28, 22, 28, 30, 33, 38, 40, 42, 40]
                        },
                        {
                            label: "Data",
                            borderColor: gradientStroke4,
                            pointBorderColor: gradientStroke4,
                            pointBackgroundColor: gradientStroke4,
                            pointHoverBackgroundColor: gradientStroke4,
                            pointHoverBorderColor: gradientStroke4,
                            pointBorderWidth: 1,
                            pointHoverRadius: 1,
                            pointHoverBorderWidth: 1,
                            pointRadius: 1,
                            fill: true,
                            backgroundColor: gradientFill4,
                            borderWidth: 1,
                            data: [40, 35, 25, 23, 40, 42, 35, 30, 28]
                        },
                        {
                            label: "Data",
                            borderColor: gradientStroke5,
                            pointBorderColor: gradientStroke5,
                            pointBackgroundColor: gradientStroke5,
                            pointHoverBackgroundColor: gradientStroke5,
                            pointHoverBorderColor: gradientStroke5,
                            pointBorderWidth: 1,
                            pointHoverRadius: 1,
                            pointHoverBorderWidth: 1,
                            pointRadius: 1,
                            fill: true,
                            backgroundColor: gradientFill5,
                            borderWidth: 1,
                            data: [2, 5, 15, 12, 16, 20, 25, 30, 35]
                        }
                        ]
                    },
                    options: {
                        animation: {
                              duration: 3000,
                              easing: "easeInOutBack"
                        },
                        legend: {
                            display: false,
                            position: "bottom"
                        },
                        scales: {
                            yAxes: [{
                                ticks: {
                                    fontColor: "rgba(0,0,0,0.5)",
                                    fontStyle: "bold",
                                    beginAtZero: true,
                                    maxTicksLimit: 300,
                                    padding: 20
                                },
                                gridLines: {
                                    drawTicks: false,
                                    display: false
                                }

                            }],
                            xAxes: [{
                                gridLines: {
                                    zeroLineColor: "transparent"
                                },
                                ticks: {
                                    padding: 20,
                                    fontColor: "rgba(0,0,0,0.5)",
                                    fontStyle: "bold"
                                }
                            }],
                            xAxes: [{
                                gridLines: {
                                    zeroLineColor: "transparent"
                                },
                                ticks: {
                                    padding: 25,
                                    fontColor: "rgba(0,0,0,0.9)",
                                    fontStyle: "bold"
                                }
                            }],
                            xAxes: [{
                                gridLines: {
                                    zeroLineColor: "transparent"
                                },
                                ticks: {
                                    padding: 20,
                                    fontColor: "rgba(0,0,0,0.9)",
                                    fontStyle: "bold"
                                }
                            }],
                            xAxes: [{
                                gridLines: {
                                    zeroLineColor: "transparent"
                                },
                                ticks: {
                                    padding: 20,
                                    fontColor: "rgba(0,0,0,0.9)",
                                    fontStyle: "bold"
                                }
                            }]
                        }
                    }
                });

                // $("#lcd-panel-review-btn .month").on('click', function(){
                //    $("#lcd-panel-review-btn span").removeClass('active');
                //    $(this).addClass('active');
                //     var data = myChart.config.data;
                //     data.datasets[0].data = temp_dataset;
                //     data.datasets[1].data = rain_dataset;
                //     data.labels = temp_lavels;
                //     myChart.update();
                // });

                // $("#lcd-panel-review-btn .year").on('click', function(){
                //    $("#lcd-panel-review-btn span").removeClass('active');
                //    $(this).addClass('active');
                //     var chart_labels = ["Jan-11", "Jan-12", "Jan-13", "Jan-14", "Jan-15", "Jan-16", "Jan-17","Jan-18", "Jan-19"];
                //     var temp_dataset = [4100, 5000, 4200, 4400, 4800, 4600, 4800, 4600, 4300];
                //     var rain_dataset = [4800, 4600, 4800, 4100, 5000, 4200, 4400, 4600, 4300];
                //     var data = myChart.config.data;
                //     data.datasets[0].data = temp_dataset;
                //     data.datasets[1].data = rain_dataset;
                //     data.labels = chart_labels;
                //     myChart.update();
                // });


          var $this = $(this);
          $this.removeClass("hidden").off("inview");
        });


    });
})(jQuery);