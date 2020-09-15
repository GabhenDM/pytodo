<template>
<div>
  <b-navbar toggleable="lg" id="navbar" type="dark" variant="info">
    <b-navbar-brand href="#">YATAP</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="#">Home</b-nav-item>
        <b-nav-item href="#">To-Do's</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item href="#">Login</b-nav-item>
        <b-nav-item href="#">Register</b-nav-item>
        <b-nav-item href="#" disabled>Logout</b-nav-item>
        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <em>User</em>
          </template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item href="#">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>
<style>
#navbar{
    background-color:#30292F !important;
}
#navbar a {
    color:white;
}
</style>