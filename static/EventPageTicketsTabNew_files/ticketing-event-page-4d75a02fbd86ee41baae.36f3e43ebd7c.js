webpackJsonp([10],{0:function(t,n,e){"use strict";e(781)},781:function(t,n,e){(function(t){"use strict";function n(t,n,e){return n in t?Object.defineProperty(t,n,{value:e,enumerable:!0,configurable:!0,writable:!0}):t[n]=e,t}t(function(){t("[data-toggle=claim-event-ownership]").click(function(e){e.preventDefault();var i=(t(this).data("event-id"),t(this).attr("href"));swal(n({title:"Can you confirm that you’re the organiser of this event?",text:"Attempts at identity theft or fraud are taken very seriously.",type:"warning",showCancelButton:!0,confirmButtonClass:"btn-danger",confirmButtonText:"Yes",closeOnConfirm:!1},"confirmButtonClass","btn-danger"),function(t){t&&(window.location=i)})})})}).call(n,e(70))}});
//# sourceMappingURL=ticketing:event-page-4d75a02fbd86ee41baae.js.map