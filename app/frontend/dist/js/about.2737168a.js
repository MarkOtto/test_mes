(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["about"],{eaad:function(e,t,s){"use strict";s.r(t);var n=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("b-row",{staticClass:"d-flex align-items-center p-4"},[s("b-col",[s("vue-good-table",{attrs:{columns:e.messagesColumn,rows:e.getInbox,"pagination-options":{enabled:!0,perPage:10,mode:"records",perPageDropdown:[10,15]}},scopedSlots:e._u([{key:"table-row",fn:function(t){return["actions"===t.column.field?s("div",{staticClass:"d-flex justify-content-center"},[s("b-button",{staticClass:"m-1",attrs:{size:"sm",variant:"success"},on:{click:function(s){return e.readCurrentMessage(t.row.id)}}},[e._v("View")])],1):e._e()]}}])})],1),s("current-message-modal")],1)},a=[],r=s("5530"),o=s("1da1"),i=(s("96cf"),s("2f62")),c=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("b-modal",{attrs:{id:"current","hide-header-close":"",centered:""},scopedSlots:e._u([{key:"modal-title",fn:function(){return[e._v(" "+e._s(e.getCurrentMessage.title)+" ")]},proxy:!0},{key:"modal-footer",fn:function(){return[s("b-button",{on:{click:e.closeModal}},[e._v("Close")])]},proxy:!0}])},[e._v(" "+e._s(e.getCurrentMessage.body)+" ")])},l=[],d={name:"CurrentMessageModal",computed:Object(r["a"])({},Object(i["b"])(["getCurrentMessage"])),methods:{closeModal:function(){this.$bvModal.hide("current")}},watch:{getCurrentMessage:function(){}}},u=d,g=s("2877"),m=Object(g["a"])(u,c,l,!1,null,"863cdd90",null),b=m.exports,f={name:"Inbox",components:{CurrentMessageModal:b},data:function(){return{columns:[{label:"To",field:"user_to.username"},{label:"Message Title",field:"title"},{label:"Actions",field:"actions",tdClass:"text-right",thClass:"text-right"}],rows:[{id:1,name:"John",age:20,createdAt:"",score:.03343},{id:2,name:"Jane",age:24,createdAt:"2011-10-31",score:.03343},{id:3,name:"Susan",age:16,createdAt:"2011-10-30",score:.03343},{id:4,name:"Chris",age:55,createdAt:"2011-10-11",score:.03343},{id:5,name:"Dan",age:40,createdAt:"2011-10-21",score:.03343},{id:6,name:"John",age:20,createdAt:"2011-10-31",score:.03343}]}},methods:{readCurrentMessage:function(e){this.$store.dispatch("GET_CURRENT_MESSAGE",e),this.$bvModal.show("current")}},mounted:function(){var e=this;return Object(o["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,e.$store.dispatch("GET_INBOX","inbox");case 2:case"end":return t.stop()}}),t)})))()},computed:Object(r["a"])(Object(r["a"])({},Object(i["b"])(["getInbox","messageType","getCurrentMessage"])),{},{messagesColumn:function(){return"sent"===this.messageType?[{label:"To",field:"user_to.username"},{label:"Message Title",field:"title"},{label:"Actions",field:"actions",tdClass:"text-right",thClass:"text-right"}]:"inbox"===this.messageType?[{label:"From",field:"user_from.username"},{label:"Message Title",field:"title"},{label:"Actions",field:"actions",tdClass:"text-right",thClass:"text-right"}]:void 0}})},h=f,p=Object(g["a"])(h,n,a,!1,null,"1c6d0c01",null);t["default"]=p.exports}}]);
//# sourceMappingURL=about.2737168a.js.map